from flask import session

import csv
import os


# GET USER CSV FILE

def get_csv_file():

    username = session.get("username")

    # DEFAULT USER

    if not username:

        file_path = "data/default.csv"

    else:

        # USER FILE

        file_path = f"data/{username}.csv"

    # CREATE FILE IF NOT EXISTS

    if not os.path.exists(file_path):

        with open(file_path, "w") as file:

            file.write("date,amount,category,type\n")

    return file_path


# READ CSV

def read_csv():

    transactions = []

    with open(get_csv_file(), "r") as file:

        reader = csv.reader(file)

        # SKIP HEADER

        next(reader)

        for index, row in enumerate(reader):

            # SKIP INVALID ROW

            if len(row) < 4:

                continue

            transactions.append({

                "id": index,

                "date": row[0],

                "amount": int(row[1]),

                "category": row[2],

                "type": row[3]

            })

    return transactions


# WRITE CSV

def write_csv(rows):

    with open(get_csv_file(), "w", newline="") as file:

        writer = csv.writer(file)

        # HEADER

        writer.writerow([

            "date",

            "amount",

            "category",

            "type"

        ])

        # DATA

        writer.writerows(rows)