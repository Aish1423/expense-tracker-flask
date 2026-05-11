class Transaction:

    def __init__(self, date, amount, category, type_):

        self.date = date
        self.amount = amount
        self.category = category
        self.type = type_

    def to_list(self):

        return [
            self.date,
            self.amount,
            self.category,
            self.type
        ]