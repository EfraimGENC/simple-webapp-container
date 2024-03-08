"""
A simple FastAPI application
Author: Efraim GENC
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """Say hello to the user"""
    return {"message": f"Hello {name}"}
