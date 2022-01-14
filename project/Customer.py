"""
The Customer class stores information about a person banking information such as
Name
Address
Date of Birth
Account Number
Pin

and a method to verify the pin
"""
import time


class Customer():

    def __init__(self, name, add, dob, accNum, pin):
        self.__name = name
        self.__address = add
        self.__dob = dob
        self.__accNum = accNum
        self.__pin = pin

    # Generate the setters and getters for the attributes
    def set_pin(self, pin):
        self.__pin = pin

    def get_pin(self):
        return self.__pin

    # Setters and getters are used to change customer information
    def set_name(self, name):
        self.__name = name

    def set_add(self, add):
        self.__address = add

    def set_dob(self, dob):
        self.__dob = dob

    def set_accNum(self, accNum):
        self.__accNum = accNum

    def get_name(self):
        return self.__name

    def get_add(self):
        return self.__address

    def get_dob(self):
        return self.__dob

    def get_accNum(self):
        return self.__accNum

    # Verify that the pin entered is the same as what the system has
    def verifyPin(self):
        # counter
        attempt = 0
        # Using a controlled while loop, if they made three attempts ,
        # lock the account and have the customer notify
        # the bank so that the bank can unlock the account.
        while attempt != 3:
            # Have the user enter their pin
            pin = int(input("Enter your pin. "))
            # Ensure that the pin is correct
            if pin == self.get_pin():
                return True
            else:
                print("Incorrect pin. Try again. ")
                attempt += 1
        else:
            print("Failed to many attempts, please contact your local bank for them to unlock your account. ")
