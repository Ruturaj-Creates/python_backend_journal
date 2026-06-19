class Dog:                      #class
    def __init__(self,name,bread,owner):  # attributes---properties
        self.name=name
        self.bread=bread
        self.owner=owner
        
    def bark(self):             #method --function in class
        print("whoof whooff")

class Owner:
    def __init__(self,name,address,contact):
        self.name=name
        self.address=address
        self.contact=contact
        
    
owner1=Owner("ruturaj","kolhapur","333-333-333")
dog1=Dog("coco","german shephard",owner1)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def greet(self):
        print(f"hello My name is {self.name} and i am {self.age} years old")

person1=Person("Akash","28")
# person1.greet()

person2=Person("Utkarsh","47")
# person2.greet()

# Accesing data from user2 to user1
class User:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
    
    def say_hi_to(self,user):
        print(f"Sending message to {user.username}:- Hi {user.username} this is {self.username}")
    
user1=User("Karan","karan@gmail.com","1234karan")
user2=User("ankita","ankita@gmail.com","1234rvd")

# user1.say_hi_to(user2)

#accessing and modifying data
user1=User("Karan","karan@gmail.com","1234karan")
# print(user1.email)

# user1.email="rvd"

# print(user1.email)


"""protected attributes"""

class Users:
    def __init__(self,username,email):
        self._username=username         # protected attribute
        self.__email=email              # private attribute

    def access_email(self):
        print(self.__email)
    
emp1=Users("rahul","rahul@gmail")
# print(emp1.username)              private attribute cannot be accessed outsite class
# print(emp1.__email)

# emp1.access_email()                 correct way to access private attrubute/getter method


"""getter and setter methods """
 
"""Getter:
The getter method is used to retrieve the value of a private attribute.
It allows controlled access to the attribute.
"""
"""
Setter: 
The setter method is used to set or modify the value of a private attribute.
It allows you to control how the value is updated,
enabling validation or modification of the data before it’s actually assigned.
"""

class Employee:
    def __init__(self,name:str,salary:int):
        self.name=name
        self._salary=salary             #private
        
    def get_salary(self):               # getter method
        return self._salary
    
    def set_salary(self,salary):       # setter method
        self._salary=salary
        return self._salary
    
empl1=Employee("ruturaj",5000)
print(empl1.get_salary())

print(empl1.set_salary(10000))
print(empl1.get_salary())