# ==========================================================
# ADVANCED PYTHON PRACTICE QUESTIONS
# ==========================================================

# Topics:
# 1. OOP
# 2. Decorators
# 3. Generators
# 4. Context Managers
# 5. Type Hints
# 6. Async/Await

# Solve each question below.
# ==========================================================


# ==========================================================
# OOP
# ==========================================================

# Q1.
# Create a Student class.

# Attributes:
# - name
# - marks

# Methods:
# - display()
# - is_pass()

# Return True if marks >= 40 otherwise False.

class Student:
    def __init__(self,name,marks:int):
        self.name=name
        self.marks=marks

    def display(self):
        return f"Name: {self.name}, Marks: {self.marks}"
    
    def is_pass(self):
        if self.marks>=40:
            return True
        else:
            return False

stud1=Student("ruturaj",45)
# print(stud1.display())
# print(stud1.is_pass())
# ----------------------------------------------------------

# Q2.
# Create a Rectangle class.

# Attributes:
# - length
# - width

# Methods:
# - area()
# - perimeter()

class Rectangle:
    def __init__(self,length:int,width:int):
        self.length=length
        self.width=width
    
    def get_area(self):
        area=self.length*self.width
        return f"area of rectagle is {area}"
    
    def get_perimeter(self):
        perimeter=2*(self.length + self.width)
        return f"perimeter of rectangle is {perimeter}"
    
rect1=Rectangle(30,15)
# print(rect1.get_area())
# print(rect1.get_perimeter())
# ----------------------------------------------------------

# Q3.
# Create a BankAccount class.

# Attributes:
# - account_holder
# - balance

# Methods:
# - deposit(amount)
# - withdraw(amount)
# - check_balance()

# Rules:
# - Cannot withdraw more than available balance.
# - Print appropriate messages.

class BankAccount:
    def __init__(self,account_holder:str,balance:int):
        self.acount_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        if amount <= 0:
            return "Amount must be positive"
        else:
            self.balance+=amount
            return self.balance

    def withdraw(self,amount):
        if self.balance>= amount:
            self.balance-=amount
            return self.balance
        else:
            return "Insufficient balance"

    def check_balance(self):
        return self.balance
    
acc1=BankAccount("ruturaj",7500)
# print(acc1.check_balance())
# print(acc1.deposit(2000))
# print(acc1.withdraw(5000))
# print(acc1.check_balance())
# ----------------------------------------------------------

# Q4.
# Create an Employee class.

# Attributes:
# - name
# - salary

# Create a Manager class inheriting Employee.

# Additional Attribute:
# - department

# Add a display() method.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        self.department=department
        super().__init__(name, salary)

    def display(self):
         return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"
    
emp1=Manager("rutu","500","IT")
# print(emp1.display())


# ----------------------------------------------------------

# Q5.
# Demonstrate Polymorphism.

# Create:
# - Dog
# - Cat
# - Cow

# Each class should implement:
# - sound()

# Loop through all objects and call sound().


# ----------------------------------------------------------

# Q6.
# Create a Library Management System.

# Create:
# - Book class
# - Library class

# Library Methods:
# - add_book()
# - remove_book()
# - display_books()


# ==========================================================
# DECORATORS
# ==========================================================

# Q7.
# Create a decorator called logger.

# Output:
# Function Started
# Function Ended

# Apply it to a greet() function.


# ----------------------------------------------------------

# Q8.
# Create a decorator called welcome_user.

# Before function:
# Welcome User

# After function:
# Thank You


# ----------------------------------------------------------

# Q9.
# Create an execution_time decorator.

# Measure and print how long a function takes to execute.


# ----------------------------------------------------------

# Q10.
# Create a decorator that prints:

# Arguments: (...)
# Keyword Arguments: {...}

# before executing the function.


# ----------------------------------------------------------

# Q11.
# Create a retry decorator.

# If a function raises an exception:
# Retry up to 3 times.

# Then raise the exception.


# ==========================================================
# GENERATORS
# ==========================================================

# Q12.
# Create a generator that yields
# the first 20 even numbers.


# ----------------------------------------------------------

# Q13.
# Create a countdown generator.

# Example:
# 10
# 9
# 8
# ...
# 1


# ----------------------------------------------------------

# Q14.
# Create a Fibonacci generator.

# Generate first 15 Fibonacci numbers.


# ----------------------------------------------------------

# Q15.
# Create a Prime Number Generator.

# Generate all prime numbers between 1 and 100.


# ----------------------------------------------------------

# Q16.
# Create an infinite counter generator.

# Output:
# 1
# 2
# 3
# ...

# Use next() to fetch values.


# ----------------------------------------------------------

# Q17.
# Create a generator that reads
# a file line by line.

# Do NOT load the entire file into memory.


# ==========================================================
# CONTEXT MANAGERS
# ==========================================================

# Q18.
# Create a custom context manager.

# Output:
# Opening File
# Working...
# Closing File

# Usage:

# with FileManager():
#     print("Working...")


# ----------------------------------------------------------

# Q19.
# Create a Database context manager.

# Output:
# Connecting...
# Working...
# Disconnecting...


# ----------------------------------------------------------

# Q20.
# Create a Timer context manager.

# Usage:

# with Timer():
#     code_here()

# Print execution time when block exits.


# ----------------------------------------------------------

# Q21.
# Create a Transaction context manager.

# If block succeeds:
# Commit Transaction

# If block fails:
# Rollback Transaction


# ==========================================================
# TYPE HINTS
# ==========================================================

# Q22.
# Type annotate:

# add(a, b)

# Return integer.


# ----------------------------------------------------------

# Q23.
# Type annotate:

# get_name()

# Return string.


# ----------------------------------------------------------

# Q24.
# Create:

# process_numbers(numbers)

# Input:
# list[int]

# Output:
# dict[str, int]


# ----------------------------------------------------------

# Q25.
# Create a User class.

# email can be:
# str OR None

# Use Optional.


# ----------------------------------------------------------

# Q26.
# Create a calculator function.

# Accept:
# int OR float

# Use Union.


# ----------------------------------------------------------

# Q27.
# Fully type annotate an Employee class.

# Include:
# - attributes
# - constructor
# - methods


# ==========================================================
# ASYNC / AWAIT
# ==========================================================

# Q28.
# Create:

# async hello()

# Output:
# Hello
# (wait 2 sec)
# World


# ----------------------------------------------------------

# Q29.
# Run two async tasks simultaneously.

# Each task should wait for 2 seconds.

# Use asyncio.gather()


# ----------------------------------------------------------

# Q30.
# Create:

# async fetch_data()

# Simulate API call:
# await asyncio.sleep(3)

# Return:
# "Data Received"


# ----------------------------------------------------------

# Q31.
# Create:

# Task A
# Task B
# Task C

# Run all concurrently using:
# asyncio.gather()


# ----------------------------------------------------------

# Q32.
# Create:

# async download_file(name)

# Simulate download using sleep().

# Run 5 downloads concurrently.


# ----------------------------------------------------------

# Q33.
# Create an Async Weather Fetcher.

# Cities:
# - Mumbai
# - Pune
# - Delhi
# - Bangalore

# Fetch all weather data concurrently.

# Simulate network calls using asyncio.sleep().


# ==========================================================
# BONUS PROJECTS
# ==========================================================

# Project 1:
# Task Management System

# Use:
# - OOP
# - Type Hints


# ----------------------------------------------------------

# Project 2:
# Library Management System

# Use:
# - OOP
# - Decorators
# - Context Managers


# ----------------------------------------------------------

# Project 3:
# Log Analyzer

# Use:
# - Generators
# - File Handling
# - Type Hints


# ----------------------------------------------------------

# Project 4:
# Async API Fetcher

# Use:
# - Async/Await
# - Decorators
# - Type Hints


# ==========================================================
# END
# # ==========================================================