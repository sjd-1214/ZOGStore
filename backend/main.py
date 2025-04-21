from pydantic import BaseModel
from typing import Union
from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def read_root():
    print("Hello World")
    return {"Hello": "World"}