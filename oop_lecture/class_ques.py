"""
Question 1: Student Class

Create a class Student.

Attributes:

name
age
course

Method:

display_info() → prints all student details
"""
class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display_info(self):
        print(f'student name is {self.name} age {self.age}')

s1=Student("ruturaj","44","arts")
s1.display_info()