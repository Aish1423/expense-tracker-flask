import csv
from utils.csv_handler import get_csv_file
from utils.csv_handler import read_csv
from utils.csv_handler import write_csv



class TransactionService:

    @staticmethod
    def get_transactions():
        return read_csv()

    @staticmethod
    def add_transaction(date, amount, category, transaction_type):

        # EMPTY LIST
        rows = []

        # READ EXISTING FILE
        with open(get_csv_file(), "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

        # ADD NEW TRANSACTION

        rows.append([

        date,
        amount,
        category,
        transaction_type

    ])

    # WRITE AGAIN

        with open(get_csv_file(), "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)
    
    @staticmethod
    def delete_transaction(id):

        rows = []

        with open(get_csv_file(), "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

        # KEEP HEADER

            header = rows[0]

            data = rows[1:]

        # REMOVE ITEM

            data.pop(id)

        # WRITE AGAIN

        with open(get_csv_file(), "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(header)

            writer.writerows(data)
    
    @staticmethod
    def update_transaction(id, date, amount, category, transaction_type):

        rows = []

        with open(get_csv_file(), "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

        # UPDATE ROW

        rows[id + 1] = [

        date,
        amount,
        category,
        transaction_type

    ]

    # WRITE AGAIN

        with open(get_csv_file(), "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        
    
    