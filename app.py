import csv
import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from api.routes import transaction_api

# CREATE FLASK APP


app = Flask(__name__)

app.secret_key = "expense_tracker"

# REGISTER API

transaction_api(app)

from models.transaction import Transaction

from services.transaction_service import TransactionService
from services.analytics import AnalyticsService

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        # SAVE USER

        with open("data/users.csv", "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([username, password])

        return redirect("/login")

    return render_template("signup.html")

# LOGIN

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        # CHECK USER

        with open("data/users.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                # MATCH USER

                if row[0] == username and row[1] == password:

                    # SAVE SESSION

                    session["username"] = username

                    return redirect("/")

        return "Invalid Username or Password"

    return render_template("login.html")

# DASHBOARD

@app.route("/")
def dashboard():

    # CHECK LOGIN

    username = session.get("username")

    # GUEST USER

    if not username:

        return render_template(

            "dashboard.html",

            logged_in=False
        )

    # GET DATA

    transactions = TransactionService.get_transactions()

    income, expense = AnalyticsService.calculate_totals()

    savings = income - expense

    # LOGIN USER DASHBOARD

    return render_template(

        "dashboard.html",

        logged_in=True,

        username=username,

        transactions=transactions,

        income=income,

        expense=expense,

        savings=savings
    )

# ADD TRANSACTION

@app.route("/add", methods=["GET", "POST"])
def add_transaction():

    # CHECK LOGIN

    if "username" not in session:

        return redirect("/login")

    # FORM SUBMIT

    if request.method == "POST":

        # GET DATA

        date = request.form["date"]

        amount = request.form["amount"]

        category = request.form["category"]

        transaction_type = request.form["type"]

        # SAVE TRANSACTION

        TransactionService.add_transaction(

            date,
            amount,
            category,
            transaction_type
        )

        # REDIRECT TO DASHBOARD

        return redirect("/")

    # OPEN PAGE

    return render_template("add.html")

# LOGOUT

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# HISTORY

@app.route("/history")
def history():

    transactions = TransactionService.get_transactions()

    return render_template(
        "history.html",
        transactions=transactions
    )

# SEARCH
@app.route("/search")
def search():

    keyword = request.args.get("keyword")

    transactions = TransactionService.get_transactions()

    filtered = []

    for t in transactions:

        if keyword.lower() in t["category"].lower():

            filtered.append(t)

    return render_template(
        "history.html",
        transactions=filtered
    )

# DELETE

@app.route("/delete/<int:id>")
def delete_transaction(id):

    # LOGIN CHECK

    if "username" not in session:

        return redirect("/login")

    # DELETE TRANSACTION

    TransactionService.delete_transaction(id)

    # REDIRECT

    return redirect("/history")


# EDIT

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_transaction(id):

    # LOGIN CHECK

    if "username" not in session:

        return redirect("/login")

    # GET TRANSACTIONS

    transactions = TransactionService.get_transactions()

    transaction = transactions[id]

    # UPDATE

    if request.method == "POST":

        date = request.form["date"]

        amount = request.form["amount"]

        category = request.form["category"]

        transaction_type = request.form["type"]

        TransactionService.update_transaction(

            id,
            date,
            amount,
            category,
            transaction_type

        )

        return redirect("/history")

    return render_template(

        "edit.html",

        transaction=transaction
    )
# REPORT

@app.route("/report")
def report():

    income, expense = AnalyticsService.calculate_totals()

    savings = income - expense

    return render_template(
        "report.html",
        income=income,
        expense=expense,
        savings=savings
    )



if __name__ == "__main__":

    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(debug=True)

    app.run(host="0.0.0.0", port=port)