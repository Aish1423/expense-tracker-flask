from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from api.routes import transaction_api

# CREATE FLASK APP

app = Flask(__name__)

# REGISTER API

transaction_api(app)

from models.transaction import Transaction

from services.transaction_service import TransactionService
from services.analytics import AnalyticsService

# DASHBOARD

@app.route("/")
def dashboard():

    transactions = TransactionService.get_transactions()

    income, expense = AnalyticsService.calculate_totals()

    return render_template(
        "dashboard.html",
        transactions=transactions,
        income=income,
        expense=expense
    )

# ADD TRANSACTION

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        transaction = Transaction(
            request.form["date"],
            request.form["amount"],
            request.form["category"],
            request.form["type"]
        )

        TransactionService.add_transaction(transaction)

        return redirect("/")

    return render_template("add.html")


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
def delete(id):

    TransactionService.delete_transaction(id)

    return redirect("/history")

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

    app.run(host="0.0.0.0", port=5000)