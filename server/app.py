from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI
from server.routes.student import router as StudentRouter

app = FastAPI()
app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get('/', tags=["Root"])
async def read_root():
    return {"message": "some shit"}

