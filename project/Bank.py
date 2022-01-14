"""
The Bank class is used to store the Customer class information.
"""

class Bank():

    def __init__(self,bankCode,bankAdd):
        self.__bankCode = bankCode
        self.__address = bankAdd


    # The accessors and mutators allows changing the bank code or bank address
    def get_bank_code(self):
        return self.__bankCode

    def get_bank_add(self):
        return self.__address

    def set_bank_code(self,code):
        self.__bankCode = code

    def set_bank_add(self,address):
        self.__address = address

    # The manages function shows the customer which bank branch manages his/her account
    def manages(self):
        print(f'The branch that manages your account is: {self.__bankCode} and the bank address is{self.__address}')

    # The modifies function modifies the bank information

    def modifies(self):
        print("Select from the following options: ")
        print("1. Change bank address. ")
        print("2. Change bank code. ")
        choice = input()
        if (choice == '1'):
            newAdd = input("Enter new address. ")
            self.set_bank_add(newAdd)
        elif choice =='2':
            newCode = input("Enter the new bank code. ")
            self.set_bank_code(newCode)
        else:
            print("You did not enter a correct option. ")



