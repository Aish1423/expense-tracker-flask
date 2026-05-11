from utils.csv_handler import read_csv


class AnalyticsService:

    @staticmethod
    def calculate_totals():

        transactions = read_csv()

        income = 0
        expense = 0

        for t in transactions:

            if t["type"] == "income":

                income += t["amount"]
            else:

                expense += t["amount"]

        return income, expense

    @staticmethod
    def get_savings():

        income, expense = AnalyticsService.calculate_totals()

        return income - expense

    @staticmethod
    def budget_alert(limit=10000):
        income, expense = AnalyticsService.calculate_totals()
        if expense > limit:
            return "⚠️ Budget Exceeded"
        else:
            return "✅ Budget Safe"
    