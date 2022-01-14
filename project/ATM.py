"""
The ATM class is the class shows which bank manages it
"""

from Bank import *
from Customer import *

class ATM():

    def __init__(self, accNum, balance,location,manageby):
        super().__init__(accNum, balance)
        self.__location =location
        self.__manager = manageby

    def identify(self):
        pass

    def transaction(self):
        pass