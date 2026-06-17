class Dog:                      #class
    def __init__(self,name,bread,owner):  # attributes---data in class
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
print(user1.email)

user1.email="rvd"

print(user1.email)


"""protected attributes"""

class Users:
    def __int__(self,username,email):
        self.username=username
        self._email=email               # protected attribute--> data -->  _

# 48.42 seconds on lecture 