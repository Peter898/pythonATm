"""
The Checking Account class inherits from the Account class.
"""
from Account import *

class CheckingsAccount(Account):
    def __init__(self, number, balance):
        super().__init__(number, balance)

    # The withdraw method over writes the withdraw method in the Account class
    def withdraw(self,amount):
        self.__new_bal = amount + self.__bal