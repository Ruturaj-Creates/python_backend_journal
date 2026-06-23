"""
Middleware is a component that executes before and after every request, 
commonly used for logging, authentication, monitoring and request processing.
"""
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def track_time(request: Request, call_next):

    start = time.time()

    response = await call_next(request)

    end = time.time()

    print(f"Time Taken: {end-start:.4f} sec")

    return response


@app.get("/users")
def get_users():
    return {"users": ["Ruturaj", "Amit"]}


@app.get("/products")
def get_products():
    return {"products": ["Laptop", "Phone"]}