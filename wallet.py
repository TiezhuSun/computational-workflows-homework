# wallet.py

class InsufficientAmount(Exception):
    pass


class Wallet(object):
    def __init__(self, initial_amount=0):
        # raise NotImplementedError
        self.balance = initial_amount

    def spend_cash(self, amount):
        # raise NotImplementedError
        if self.balance < amount:
            raise InsufficientAmount
        self.balance -= amount

    def add_cash(self, amount):
        # raise NotImplementedError
        self.balance += amount
