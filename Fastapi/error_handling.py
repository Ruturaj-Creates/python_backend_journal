
"""
We use HTTPException because it returns proper HTTP status codes and standardized error responses, 
making APIs easier for clients to understand and handle."""

from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel,Field

app =FastAPI()

@app.get("/user/{id}")
def get_user(id:int):
    if id> 10:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    else:
        return {
            "id":id
            }
    
"""
200 → Success

201 → Resource Created

400 → Bad Request

401 → Unauthorized

403 → Forbidden

404 → Not Found

500 → Internal Server Error
"""