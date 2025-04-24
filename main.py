from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# from models import models
from pydantic import BaseModel

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@app.get('/')
def home():
    return ("{'message': 'Welcome to the Game Store API'}")
    