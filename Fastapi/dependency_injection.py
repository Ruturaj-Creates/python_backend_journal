#Dependency injection
"""Dependency Injection is a design pattern where FastAPI automatically provides required dependencies 
(database connection, authentication, configuration, etc.) to a route using Depends()."""

"Depends() reduces code duplication, improves reusability, and lets FastAPI automatically manage dependencies."

from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field

app =FastAPI()

def get_name():
    return "Ruturaj"

@app.get("/")
def home(name=Depends(get_name)):
    return {
        "name":name
    }
