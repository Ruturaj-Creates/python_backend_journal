"""
class attributes
    Defined within the class block but outside of methods
    Shared among all instances of the class
    Accessed using the class name or ANY instance
"""

"""
Instance Attributes
    Defined within methods, typically the __init__ constructor
    Specific to each instance of the class
    Accessed using an instance of the class
"""

class User:
    total_user=0                                        # static attribute ---> used when values are shared amoong all instances

    def __init__(self,name,email):                      # instance attribute ---> unique to each instace - unique data is stored
        self.name=name
        self.email=email
        User.total_user+=1

    def display_user(self):
        print(f"User is {self.name} and email is {self.email}")

u1=User("aniket","ani@123")
u2=User("kiran","kn@900")

# u1.display_user()
# print(u1.total_user)


