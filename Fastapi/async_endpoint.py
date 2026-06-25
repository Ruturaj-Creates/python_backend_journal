from fastapi import FastAPI
import asyncio

app=FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {"msg":"done"}


"""
Can every FastAPI endpoint be async?

Answer:

Yes, but it is useful mainly when the endpoint performs I/O operations.

For simple calculations or quick logic, a normal def endpoint is also fine."""