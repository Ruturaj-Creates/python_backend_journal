"""
Question 1

Create a class Employee.

Attributes:
- emp_id
- name
- salary

Methods:
- get_details()

Create 2 employee objects and print their details.
"""
class Employee:
    def __init__(self,emp_id:int,name:str,salary:int):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary

    def get_details(self):
        return {
            "employe name":self.name,
            "emp id":self.emp_id,
            "salary":self.salary
        }
    
emp1=Employee(22,"Aniket",25000)
emp2=Employee(55,"rahul",60000)

# print(emp1.get_details())
# print(emp2.get_details())

"""
Question 2

Create a class Student.

Constructor should accept:
- roll_no
- name
- marks

Methods:
- display_student()

Create 3 student objects and display their information.
"""
class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks

    def display_student(self):
        return f"student name is {self.name}, rollno is {self.roll_no} and marks is {self.marks}"
    
stud1=Student(12,"atharva",30)
stud2=Student(14,"ruturaj",99)

# print(stud1.display_student())

"""
Question 3

Create a class Product.

Attributes:
- product_id
- product_name
- price

Methods:
- apply_discount(discount_percent)
- display_product()

Create a product object and apply a 10% discount.
Print updated price.
"""
class Product:
    def __init__(self,prod_id,prod_name,price):
        self.prod_id=prod_id
        self.prod_name=prod_name
        self.price=price

    def display_product(self):
        print(f"product name is {self.prod_name} and price is {self.price}")

    def apply_discount(self,discount_percent:int):
        discount=discount_percent/100*self.price
        discounted_price=self.price-discount
        print(f"final price after discount is {discounted_price}")

prod1=Product(11,"toothbrush",1500)
# prod1.display_product()
# prod1.apply_discount(10)

"""
Question 4

Create a class BankAccount.

Attributes:
- account_number
- holder_name
- balance

Methods:
- deposit(amount)
- withdraw(amount)
- check_balance()

Create an account object and perform multiple transactions.
"""
class BankAccount:
    def __init__(self,acc_num,holder_name,balance):
        self.acc_num=acc_num
        self.holder_name=holder_name
        self.balance=balance

    def check_balance(self):
        return self.balance
    
    def deposit(self,amt):
        self.balance=self.balance+amt
        return f"deposited"
    
    def withdraw(self,amt):
        self.balance=self.balance-amt
        return "Withdraw"
    
bk1=BankAccount(123,"ruturaj",500)
# print(bk1.check_balance())
# print(bk1.deposit(500))
# print(bk1.check_balance())
# print(bk1.withdraw(100))
# print(bk1.check_balance())

"""
Question 5

Create a class Book.

Attributes:
- title
- author
- price

Methods:
- display_book()

Create a list containing 5 Book objects.

Loop through the list and print details of all books.
"""
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display_book(self):
        print(f"book details: title = {self.title}, author = {self.author} , price = {self.price}")

b1=Book("alchemist","ruturaj desai",599)
# b1.display_book()