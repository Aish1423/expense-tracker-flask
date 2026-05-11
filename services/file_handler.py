import os   
from config import FILE_PATH

def initialize_file():
    if not os.path.exists(FILE_PATH):

        with open(FILE_PATH, "w") as f:
            f.write("date, amount,category,type\n")


def write_data(transaction):
    with open(FILE_PATH, "a") as f:
        f.write(transaction.to_csv() + "\n")

def read_data():

    try:
        with open(FILE_PATH) as f:
            lines = f.readlines()
            return [

                line.strip().split(",")
                for line in lines[1:]
            ]
    except FileNotFoundError:
            return []