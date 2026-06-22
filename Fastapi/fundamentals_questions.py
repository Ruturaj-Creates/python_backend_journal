"""
========================================
FASTAPI FUNDAMENTALS - ROUND 1
========================================
"""

"""
Q1. What is FastAPI?

Answer:
FastAPI is a modern, high-performance Python web framework used for building APIs. 
It supports async programming, automatic data validation using Pydantic, 
and auto-generated API documentation through Swagger UI.
"""


"""
Q2. What command is used to run a FastAPI application?

Answer:
uvicorn main:app --reload
"""



"""
Q3. What is the purpose of app = FastAPI() ?

Answer:
app = FastAPI() creates the FastAPI application instance. 
It acts as the main entry point where we register routes, middleware, dependencies, and application configurations.
"""



"""
Q4. Difference between GET and POST?

Answer:
both are http methods . get is used to get/fetch data while post is used when we want to create data/something 
"""



"""
Q5. Difference between PUT and PATCH?

Answer:
Both are HTTP methods, put is used when we want to update entire data and patch as name suggests is used to update selective parts
"""



"""
Q6. What is a Path Parameter?

Give an example URL.

Answer:
Path parameters are values passed directly in the URL path and are usually used to identify a specific resource.
eg. /users/{user_id}
"""



"""
Q7. What is a Query Parameter?

Give an example URL.

Answer:
Its a type of parameter by which user can request data . in query parameter data is passed after ? 
eg /user?city=delhi

"""



"""
Q8. Which parameter is mandatory?

@app.get("/users/{id}")

OR

@app.get("/users")
def get_users(city:str=None)

Answer:
path parameter which is id is mandatory as without id it will fail whereas in 2nd city is optional
"""



"""
Q9. What is Request Body?

Answer:
Request Body is the data sent by the client to the server, usually in JSON format, commonly used in POST, PUT and PATCH requests.
eg.
{
  "name":"Ruturaj",
  "age":23
}
"""



"""
Q10. Why do we use Pydantic Models in Request Body?

Answer:
we use pydantic models in request body to validate coming data .
used for:-
Validation
Type checking
Automatic error messages
Serialization
"""

"""
========================================
FASTAPI FUNDAMENTALS - ROUND 2
PREDICT OUTPUT
========================================
"""

"""
Q11.

@app.get("/users/{id}")
def get_user(id:int):
    return {"id":id}

Request:
/users/101

Output:
"id":101
"""



"""
Q12.

@app.get("/products")
def get_product(name:str):
    return {"name":name}

Request:
/products?name=Laptop

Output:
"name":Laptop
"""



"""
Q13.

from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    return user

Request:

{
    "name":"Ruturaj",
    "age":23
}

Output:
{
    "name":"Ruturaj",
    "age":23
}
"""



"""
Q14.

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
"name":"Ruturaj"
"""

"""
========================================
FASTAPI FUNDAMENTALS - ROUND 3
CODING QUESTIONS
========================================
"""

"""
Q15.

Create a GET route:

/hello

Response:

{
    "message":"Hello World"
}

Write Code Below:
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def greet():
    return {
        "message":"hello world"
    }




"""
Q16.

Create a Path Parameter route:

/student/{id}

Return:

{
    "student_id": id
}

Write Code Below:
"""
from fastapi import FastAPI

app=FastAPI()

@app.get("/student/{id}")
def get_id(id:int):
    return {
        "student":id
    }





"""
Q17.

Create a Query Parameter route:

/search?name=Ruturaj

Return:

{
    "name":"Ruturaj"
}

Write Code Below:
"""
from fastapi import FastAPI

app=FastAPI()

@app.get("/search")
def get_data(name:str):
    return {
        "name":"Ruturaj"
    }




"""
Q18.

Create a Pydantic Model:

{
    "name":"Laptop",
    "price":50000
}

Create a POST endpoint using this model.

Write Code Below:
"""
from fastapi import FastAPI()
from pydantic import BaseModel
app=FastAPI()


class User(BaseModel):
    name:str
    price:int

@app.post("/user")
def create_user(user:User):
    return user