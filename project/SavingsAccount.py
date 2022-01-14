"""
The Savings Account class inherits from the Account class.
"""
from Account import *
class SavingsAccount(Account):

    def __init__(self, number, balance):
        super().__init__(number, balance)


