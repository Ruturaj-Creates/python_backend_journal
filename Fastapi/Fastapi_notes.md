# FastAPI Revision Notes

---

# PHASE 3 : FASTAPI

FastAPI is a modern Python web framework used to build APIs.

Features:
- Fast performance
- Automatic Swagger Documentation
- Type Hints Support
- Validation using Pydantic
- Async Support

Installation:

```bash
pip install fastapi uvicorn
```

Run Server:

```bash
uvicorn main:app --reload
```

main = filename
app = FastAPI() object

---

# ==========================
# BASICS
# ==========================

# Project Structure

## Simple Structure

```text
project/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
└── requirements.txt
```

---

## Production Structure

```text
project/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── database/
│   └── core/
│
└── requirements.txt
```
## What Each File Does

### main.py

Application entry point.

```python
from fastapi import FastAPI

app = FastAPI()
```

Responsible for:

- Creating FastAPI app
- Registering routes
- Starting application

---

### models.py

Contains database models.

Example:

```python
class User:
    pass
```

In real projects:

- SQLAlchemy models
- Database tables

---

### schemas.py

Contains Pydantic models.

Example:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int
```

Used for:

- Request validation
- Response validation

---

### database.py

Database connection setup.

Example:

```python
from sqlalchemy import create_engine

engine = create_engine(DB_URL)
```

Responsible for:

- DB connection
- Session creation

---

### requirements.txt

Stores project dependencies.

Example:

```text
fastapi
uvicorn
sqlalchemy
psycopg2-binary
```

Install:

```bash
pip install -r requirements.txt
```

---

# Production Structure Explained

```text
app/
├── main.py
├── routes/
├── models/
├── schemas/
├── services/
├── database/
└── core/
```

### routes/

Contains API endpoints.

Example:

```python
@router.get("/users")
def get_users():
    pass
```

---

### models/

Database table definitions.

Example:

```python
class User(Base):
    pass
```

---

### schemas/

Pydantic request/response models.

Example:

```python
class UserCreate(BaseModel):
    pass
```

---

### services/

Business logic.

Example:

```python
def create_user():
    pass
```

Keeps routes clean.

---

### database/

Database configuration.

Example:

```python
engine.py
session.py
```

---

### core/

Application-wide settings.

Examples:

```text
config.py
security.py
constants.py
```

---

# Interview Question

Why separate Routes, Services, Schemas and Models?

Answer:

- Better code organization
- Easier maintenance
- Reusable business logic
- Scalable architecture
- Team-friendly structure

---

# 2. Creating FastAPI Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome"}
```

Output:

{
    "message":"Welcome"
}

---

# 3. Routing

Routing means mapping URL to function.

GET

```python
@app.get("/users")
def get_users():
    return {"users":[]}
```

POST

```python
@app.post("/users")
def create_user():
    return {"message":"User Created"}
```

PUT

```python
@app.put("/users/{id}")
def update_user(id:int):
    return {"message":"Updated"}
```

DELETE

```python
@app.delete("/users/{id}")
def delete_user(id:int):
    return {"message":"Deleted"}
```

---

# HTTP Methods

GET
- Fetch Data

POST
- Create Data

PUT
- Replace Entire Record

PATCH
- Partial Update

DELETE
- Delete Record

---

# 4. Path Parameters

Value passed inside URL.

```python
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id}
```

Request:

/users/10

Response:

{
    "user_id":10
}

---

# Multiple Path Parameters

```python
@app.get("/users/{user_id}/orders/{order_id}")
def get_order(user_id:int,order_id:int):
    return {
        "user_id":user_id,
        "order_id":order_id
    }
```

---

# 5. Query Parameters

Passed after ?

Example:

/users?city=Pune

```python
@app.get("/users")
def get_users(city:str):
    return {"city":city}
```

Request:

/users?city=Pune

Response:

{
    "city":"Pune"
}
```

Optional Query Parameter

```python
from typing import Optional

@app.get("/users")
def get_users(city:Optional[str]=None):
    return {"city":city}
```

---

# Difference

Path Parameter

/users/10

Query Parameter

/users?city=Pune

---

# 6. Request Body

Used when client sends data.

```python
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    return user
```

Request

```json
{
    "name":"Ruturaj",
    "age":23
}
```

Response

```json
{
    "name":"Ruturaj",
    "age":23
}
```

---

# 7. Response Model

Controls output sent to client.

```python
from pydantic import BaseModel

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
```

Response

```json
{
    "name":"Ruturaj"
}
```

age hidden automatically.

Benefits

- Data Validation
- Hide Sensitive Data
- Consistent Response

---

# Swagger Documentation

Auto Generated

URL

http://127.0.0.1:8000/docs

Alternative

http://127.0.0.1:8000/redoc

---

# FastAPI Request Lifecycle
```text
Client
 ↓
Route
 ↓
Validation
 ↓
Function
 ↓
Response Model
 ↓
Client
```
---

# Interview Questions

1. What is FastAPI?
2. Why is FastAPI faster than Flask?
3. Difference between PUT and PATCH?
4. Difference between Query and Path Parameters?
5. What is Request Body?
6. What is Response Model?
7. What is Swagger Documentation?
8. Why use Pydantic?
9. What is Uvicorn?
10. What is ASGI?

---

