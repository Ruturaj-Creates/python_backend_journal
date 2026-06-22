"""
========================================
FASTAPI FUNDAMENTALS PRACTICE SET 2
========================================
"""
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()



"""
Q1.

Create a GET route:

/welcome

Response:

{
    "message":"Welcome to FastAPI"
}
"""
@app.get("/welcome")
def great():
    return{
        "message":"welcome to fastapi"
    }



"""
Q2.

Create a GET route:

/student/{student_id}

Return:

{
    "student_id": student_id
}
"""
@app.get("/student/{student_id}")
def get_detail(student_id:int):
    return {
        "student_id":student_id
    }


"""
Q3.

Create a GET route:

/employee/{emp_id}

Return:

{
    "employee_id": emp_id
}
"""


@app.get("/employee/{employee_id}")
def get_emp(employee_id:int):
    return {
        "employee_id":employee_id
    }


"""
Q4.

Create a GET route:

/search

Accept query parameter:

name:str

Request:

/search?name=Ruturaj

Response:

{
    "name":"Ruturaj"
}
"""
@app.get("/search")
def get_name(name:str):
    return {
        "name":name
    }

"""
Q5.

Create a GET route:

/products

Accept query parameter:

category:str

Request:

/products?category=electronics

Response:

{
    "category":"electronics"
}
"""
@app.get("/products")
def get_prod(category:str):
    return {
        "category":category
    }


"""
Q6.

Create a GET route:

/users/{user_id}

Also accept query parameter:

city:str

Request:

/users/101?city=Pune

Response:

{
    "user_id":101,
    "city":"Pune"
}
"""
@app.get("/user/{user_id}")
def get_usr(user_id:int,city:str):
    return {
        "user_id":user_id,
        "city":city
    }

"""
Q7.

Create a GET route:

/square/{num}

Return:

{
    "number": num,
    "square": num*num
}
"""



"""
Q8.

Create a GET route:

/add

Accept query parameters:

a:int
b:int

Request:

/add?a=10&b=20

Response:

{
    "result":30
}
"""



"""
Q9.

Create a Pydantic model:

Book

Fields:

title:str
price:int

Create POST endpoint:

/book

Return incoming data.
"""



"""
Q10.

Create a Pydantic model:

Student

Fields:

name:str
age:int

Create POST endpoint:

/student

Return incoming data.
"""



"""
Q11.

Predict Output

@app.get("/users/{id}")
def get_user(id:int):
    return {"id":id}

Request:

/users/55

Output:
"""



"""
Q12.

Predict Output

@app.get("/search")
def search(city:str):
    return {"city":city}

Request:

/search?city=Pune

Output:
"""



"""
Q13.

Predict Output

class Product(BaseModel):
    name:str
    price:int

@app.post("/product")
def create_product(product:Product):
    return product

Request:

{
    "name":"Laptop",
    "price":50000
}

Output:
"""



"""
Q14.

Predict Output

class UserResponse(BaseModel):
    name:str

@app.get(
    "/user",
    response_model=UserResponse
)
def get_user():
    return {
        "name":"Ruturaj",
        "age":23
    }

Output:
"""



"""
Q15.

Identify Error

@app.get("/employee/{id}")
def get_employee():
    return {"id":id}

What is wrong?
"""



"""
Q16.

Identify Error

@app.get("/search?name=Ruturaj")
def search(name:str):
    return {"name":name}

What is wrong?
"""