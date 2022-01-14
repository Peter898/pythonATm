"""
The ATM Transaction class inherits the Account class attributes

"""
from Account import *


class ATMTransaction(Account):

    def __init__(self, number, balance, transactionID, date):
        super().__init__(number, balance)
        self.__transID = transactionID
        self.__date = date

    # The modify function asks the user what they want to do
    def modifies(self):
        print("Select from one of the following options. ")
        print("1.Deposit money. ")
        print("2.Withdraw money. ")
        print("3.View account. ")
        print("4.Exit. ")
        choice = input()
        if choice == '1':
            amount = int(input("Enter the amount you want to deposit. "))
            Account.deposit(self, amount)
            print()
            ATMTransaction.modifies(self)
        elif choice == '2':
            amount = int(input("Enter the amount you want to deposit. "))
            Account.withdraw(self, amount)
            print()
            ATMTransaction.modifies(self)
        elif choice =='3':
            print("Account Number \t\t\tBalance")
            print("----------------------------------")
            print(Account.get_num(self), "\t\t\t\t\t", Account.get_bal(self))
            print()
            ATMTransaction.modifies(self)
        else:
            print("Exiting the application. ")


    # Create the setters and getters for the class
    def get_date(self):
        return self.__date


    def get_transaction(self):
        return self.__transID

# def __str__(self):
#     return f'Transaction ID: {self.__transID} \nDate: {self.__date} \nType: {self.__type}' \
#            f'Amount: {self.__amount} \nPost Balance: {self.__postBal}'
