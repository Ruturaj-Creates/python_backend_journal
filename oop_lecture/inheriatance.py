"""
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class)
 to inherit attributes and methods from another class (called a parent or base class).
"""

class Vehicle:
    def __init__(self,cc,color,brand):
        self.cc=cc
        self.color=color
        self.brand=brand

    def start(self):
        print("vehicle is starting")

    def stop(self):
        print("vehicle is stopping")

class Car(Vehicle):
    def __init__(self, cc, color, brand,doors):
        super().__init__(cc, color, brand)
        self.doors=doors

class Bike(Vehicle):
    def __init__(self, cc, color, brand,category):
        super().__init__(cc, color, brand)
        self.category=category

car1=Car("1200","mlue","ford","2")
bike1=Bike(650,"white","royal enfield","cafe racer")
# car1.start()
# car1.stop()
# print(car1.__dict__)

# bike1.start()
# bike1.stop()
# print(bike1.__dict__)
        