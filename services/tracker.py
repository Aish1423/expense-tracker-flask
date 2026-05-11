from services.file_handler import read_data, write_data

def add_transaction(transaction):

    write_data(transaction)

def monthly_report(month):
    data = read_data()

    filtered = [
        d for d in data 
        if d[0].split("-")[1] == month]

    income = sum(
        float(x[1]) for x in filtered 
        if x[3] == "income")

    expense = sum(
        float(x[1]) for x in filtered 
        if x[3] == "expense")

    return income, expense