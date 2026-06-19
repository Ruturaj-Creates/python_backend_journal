"""
static method
    @staticmethod-
            A static method in Python is a method defined inside a class that does not depend on any instance or class data.
              It is used when a function logically belongs to a class but does not need access to self or cls.
              Static methods help organize related utility functions inside a class without creating objects.
"""
class Calc:
    @staticmethod           #@staticmethod: Declares the method as static
    def add(a, b):          #parameters: Normal function arguments (no self or cls)
        return a + b

res = Calc.add(2, 3)
print(res)

"""
Instance methods use a self parameter pointing to an instance of the class.
They can access and modify instance state through self and class state through self.__class__.
These are the most common methods in Python classes.
"""
"""
Class methods use a cls parameter pointing to the class itself.
They can modify class-level state through cls, 
but they can’t modify individual instance state.

"""
# static vs instance method

class BankAcount:
    MIN_BALANCE=100

    def __init__(self,owner,balance=0):             # instance attribute
        self.owner=owner
        self._balance=balance

    def deposit(self,amount):                                                       # instance method
        if amount>0:
            self._balance+=amount
            print(f"{amount}₹ got credited , total balance is {self._balance}")
        else:
            print("error please inter valid amount")

    @staticmethod                                                                   #static method
    def is_valid_interest(rate):
        return 0<=rate<=5
    
acc1=BankAcount("vinita",800)
# acc1.deposit(200)
# print(BankAcount.is_valid_interest(2))
