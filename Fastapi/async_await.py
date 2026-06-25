"""
Asyncio is a Python library that is used for concurrent programming, including the use of async iterator in Python. 
It is not multi-threading or multi-processing. 
Asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web servers, 
database connection libraries, distributed task queues, etc"""

import asyncio
import time
from fastapi import FastAPI

app=FastAPI()
#normal function
def task1():
    time.sleep(3)
    print("task1 started")

def task2():
    time.sleep(3)
    print("task 2 started")

# task1()
# task2()

#with asyc example
async def task1():
    await asyncio.sleep(3)
    print("Task 1")

async def task2():
    await asyncio.sleep(3)
    print("Task 2")

async def main():
    await asyncio.gather(task1(), task2())

# asyncio.run(main())

#async eg in fastapi
@app.get("/")
async def get_home():
    await asyncio.sleep(3)
    return {"msg":"done"}