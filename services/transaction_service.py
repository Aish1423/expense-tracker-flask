import csv

from utils.csv_handler import read_csv
from utils.csv_handler import write_csv

CSV_FILE = "data/data.csv"

class TransactionService:

    @staticmethod
    def get_transactions():
        return read_csv()

    @staticmethod
    def add_transaction(transaction):
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(transaction.to_list())
    
    @staticmethod
    def delete_transaction(id):

        transactions = read_csv()

        transactions.pop(id)

        rows = []

        for t in transactions:

            rows.append([
                t["date"],
                t["amount"],
                t["category"],
                t["type"]
            ])
        write_csv(rows)

        
    