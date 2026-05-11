import csv
CSV_FILE = "data/data.csv"

def read_csv():
    transactions = []
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for index, row in enumerate(reader):
            if len(row) <4:
                continue

            transactions.append({
                 "id": index,
                "date": row[0],
                "amount": int(row[1]),
                "category": row[2],
                "type": row[3]
            }) 

    return transactions

def write_csv(rows):
    with open(CSV_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "date",
            "amount",
            "category",
            "type"
        ])
        writer.writerows(rows)

