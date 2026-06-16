# # ============================================================
# # Phase 1 - Day 1 (Python Basics Revision)
# # Solve all questions below in this file.
# # ============================================================


# # ============================================================
# # Variables & Data Types
# # ============================================================

# # Q1
# # Create variables storing:
# # - Name
# # - Age
# # - Height
# # - Is_Student
# #
# # Print both the value and datatype of each variable.
name="ruturaj"
age=35
height=153.55
is_student=True
print(name,type(name))
print(age,type(age))
print(height,type(height))
print(is_student,type(is_student))

# Q2
# Take a number as input from the user.
#
# Print:
# - Original value
# - Original datatype
# - Converted float value
# - Converted datatype

num=int(input("type a number:-"))
print(num)
print(type(num))
print(float(num))
print(type(float(num)))

# Q3
# Swap two variables without using a third variable.
#
# Example:
# a = 10
# b = 20
#
# Output:
# a = 20
# b = 10
a=10
b=20
a,b=b,a
print("b",b)
print("a",a)

# ============================================================
# Operators
# ============================================================

# Q4
# Given:
# a = 17
# b = 5
#
# Print:
# - Addition
# - Subtraction
# - Multiplication
# - Division
# - Floor Division
# - Modulus
# - Power
a = 17
b = 5
print(f"add {a+b}")
print(f"sub {a-b}")
print(f"multiplication {a*b}")
print(f"divsion {a/b}")
print(f"floor div {a//b}")
print(f"modulus {a%b}")
print(f"power {a**b}")

# Q5
# Check whether a number is even or odd.
num=10
if num%2==0:
    print("even")
else:
    print("odd")

# Q6
# Check whether a number is divisible by both 3 and 5.
num = 9
if num%3==0 and num%5==0 :
    print("divisible by both")
else:
    print("not divisible by both")

# ============================================================
# Conditional Statements
# ============================================================

# Q7
# Input marks and print grade:
#
# 90+      -> A
# 75-89    -> B
# 60-74    -> C
# Below 60 -> Fail
marks=99
if marks >=90:
    print("A+")
elif marks<=89 and marks>=75:
    print("B")
elif marks>=60 and marks<=74:
    print("c")
else:
    print("Fail")

# Q8
# Find the largest among three numbers.
a=10
b=4
c=15
if a>b:
    if a>c:
        print(f"{a} is greater")
elif b>a:                                             #need pratice
    if b>a:
        print(f"{b} is greater")
else:
    print(f"{c} is greater")
#or
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# Q9
# # Check whether a year is a leap year.
year=2002
if year % 400 == 0:
    print("leap")
elif year % 100 == 0:
    print(" not leap")
elif year % 4 == 0:
    print("leap")
else:
    print(" not leap")

# ============================================================
# Loops
# ============================================================

# Q10
# Print numbers from 1 to 20 using a loop.
for i in range(1,11,1):
    print(i)


# Q11
# Print all even numbers from 1 to 50.
for num in range(1,51,1):
    if num%2==0:
        print(num)

# Q12
# Find the sum of numbers from 1 to n.
#
# Example:
# n = 5
#
# Output:
# 15

n = 4
sum=0
for num in range(1,n+1,1):
    sum+=num
print(sum)

# Q13
# Print the multiplication table of a given number.
#
# Example:
# 5 x 1 = 5
# ...
# 5 x 10 = 50

num=2
for i in range(1,11,1):
    print(f"{num}X{i}={i*num}")

# Q14
# Count the number of vowels in a string.
#
# Example:
# Input:
# hello world
#
# Output:
# 3
string="hello world"
vow="aeiouAEIOU"
count=0
for i in string:
    if i in vow:
        count+=1
print(f"total vowels = {count}")

# ============================================================
# Functions
# ============================================================

# Q15
# Create a function that returns the square of a number.
def square(a):
    sq=a**2
    print( sq)

square(2)

# Q16
# Create a function that checks whether a number is prime.
#
# Return:
# True if prime
# False otherwise
def num(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print("false")
                break
        else:
            print("True")
    else:
        print("false")
num(7)
# Q17
# Create a function that accepts a list and returns the largest value.
#
# Example:
# Input:
# [5, 8, 2, 10]
#
# Output:
# 10

def num(a):
    lr=a[0]
    for i in a:
        if i > lr:
            lr=i
    print(lr)

num([2,4,8,11,3,7,9])  

# ============================================================
# Modules & Packages
# ============================================================

# Q18
# Import the math module and print:
# - Square root of 64
# - Value of pi
import math
square=math.sqrt(64)
print(square)
pie=math.pi
print(pie)

# Q19
# Import only factorial from math and calculate factorial of 5.
from math import factorial
fct=factorial(3)
print(fct)


# ============================================================
# Virtual Environments (Theory)
# ============================================================

# Q20
#
# Answer the following in comments:
#
# 1. Why do we use virtual environments?
"""as name suggests it clear a separate space in the root directory / project where we can download various different packages 
and their different versions as per our project requirement"""
#
# 2. Difference between global packages and virtual
#    environment packages.
"""global packages are packages that are installed globally into the computer and virtual env packages are packages that are installed
into the virtual env in venv we can dowload packages of same packages along with their different versions , whereas in global this 
might create conflict"""

3. Commands to:
#    - Create a virtual environment
python -m venv venv
#    - Activate a virtual environment
\venv\scripts\activate
#    - Deactivate a virtual environment
deactivate

