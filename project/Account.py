"""
The Account class is what lets the user decide on what do to in the account.
Lets user pick which account they want to do something to
"""

class Account():
    def __init__(self,number, balance):
        self.__number = number
        self.__bal = balance

    def deposit(self,amount):
        self.__bal = amount + self.__bal
        print(f'Your new balance is {self.__bal}')

    def withdraw(self,amount):
        self.__bal = self.__bal - amount
        print(f'Your new balance is {self.__bal}')


    # Create the setters and getters

    def get_num(self):
        return self.__number

    def get_bal(self):
        return self.__bal

    def set_num(self,number):
        self.__number = number

    def set_bal(self,bal):
        self.__bal = bal