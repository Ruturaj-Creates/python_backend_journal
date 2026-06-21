"""
polymorphism means "many forms" and allows the same method, 
function or operator to behave differently depending on the object or data it works with. 
This flexibility helps create more reusable, maintainable and scalable code.

Real-Life Example: In a backend payment system, 
multiple payment options are available such as Credit Card, UPI, NetBanking and Wallet. 
All payment types use a common method named processPayment() but different implementations:

Credit Card Payment: validates card, talks to bank API
UPI Payment: redirects to UPI gateway
Wallet Payment: checks wallet balance
NetBanking Payment: redirects to bank login
The method name remains the same, but the action changes based on the payment type.
"""

class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

    def start(self):
        print("vehicle is starting")

    def stop(self):
        print("vehicle is stopping")

class Car(Vehicle):
    def __init__(self, brand, year,category):
        super().__init__(brand, year)
        self.category=category

    def start(self):
        print(f"{self.brand} car is starting")

    def stop(self):
        print(f"{self.stop} car is stopping")

class Bike(Vehicle):
    def __init__(self, brand, year,engine_cc):
        super().__init__(brand, year)
        self.engine_cc=engine_cc

    def start(self):
        print(f"{self.brand} bike is starting")

    def stop(self):
        print(f"{self.brand} bike is stopping")

vehicles=[Bike("Honda","2020","650"),
Car("kia",'2024',"sports")]

for vehicle in vehicles:
    if isinstance(vehicle,Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.year} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()