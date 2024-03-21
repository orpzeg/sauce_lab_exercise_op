from decimal import Decimal


class Money:
    def __init__(self, amount, currency):
        self.amount = Decimal(amount)
        self.currency = currency

    def __repr__(self):
        return f"{self.currency} {self.amount:.2f}"