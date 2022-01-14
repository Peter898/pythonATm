"""
Tests the Customer, Account and ATMTransaction class
"""

from ATMTransactions import *
from Customer import *
from Account import *

def main():
    # Test the constructor in the Customer class
    # Create the instance and its attributes
    cus1 = Customer("John","90 Waterside Plaza", "02/22/1999",23091,1234)
    # Using the Account class pass in the required attributes
    acc1 = Account(cus1.get_accNum(), 0)

    # Have the user login with their pin
    # Check if the pin is correct
    if cus1.verifyPin() == True:
        print("Logging in...")
        print("--------------")
        time.sleep(3)
        # Tests the ATMTransaction Class
        trans1 = ATMTransaction(acc1.get_num(),acc1.get_bal(),1,"02/22/2021")
        trans1.modifies()

main()