from flask import jsonify

from services.transaction_service import TransactionService


def transaction_api(app):

    @app.route("/api/transactions")
    def api_transactions():

        transactions = TransactionService.get_transactions()

        return jsonify(transactions)