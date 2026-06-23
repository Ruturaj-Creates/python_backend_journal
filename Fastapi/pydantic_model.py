#create pydantic model
from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr

app=FastAPI()

class Book(BaseModel):
    title:str=Field(min_length=4,max_length=20)
    price:int=Field(gt=0)

@app.post("/book")
def create_book(book:Book):
    return{
        "title":book.title,
        "price":book.price
    }
# emailstr

class User(BaseModel):
    name:str
    email:EmailStr

@app.post("/user")
def create_user(user:User):
    return{
        user
    }