from datetime import datetime

class Employee:
    def __init__(self,name,email,salary):
        self.name=name
        self._email=email
        self._salary=salary
    
    @property                                       # decorator
    def email(self):                                # getter properties
        print(f"email accessed at {datetime.now()}")
        return self._email
    
    @email.setter
    def email(self,new_email):
        if "@" not in new_email:
            raise ValueError("Invalid email")
        else:
            print(f"email updated at {datetime.now()}")
            self._email=new_email

emp1=Employee("Pratik","pratik@gmail.com","5000")
# print(emp1.name)

# print(emp1.email)
# emp1.email="newmail@gmail.com"
# print(emp1.email)


# 1.15 min lec on instance attributes
