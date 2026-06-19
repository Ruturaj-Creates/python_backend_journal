# Encapsulation
"""
Encapsulation is one of the core concepts of Object Oriented Programming (OOP).

The idea of encapsulation is to bind the data members and methods into a single unit.
Helps in better maintainability, readability and usability as we do not need to explicitly pass data members to member methods
Helps maintain data integrity by allowing validation and control over the values assigned to variables.
"""
# eg
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
# print(emp.name)       
# print(emp.__salary)

#--
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount must be positive")
        else:
            self.__balance+=amount
    
    def withdraw(self,amount):
        if amount> self.__balance:
            raise ValueError("Insufficent balance")
        if amount<=0:
            raise ValueError("Enter correct amount")
        self.__balance-amount

acc1=BankAccount("harry",5000)
print(acc1.get_balance())
acc1.deposit(2000)
print(acc1.get_balance())
acc1.withdraw(100)
print(acc1.get_balance())