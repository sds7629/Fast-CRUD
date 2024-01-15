from fastapi import FastAPI
from models import BoardModel
from db.connection import engine

BoardModel.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"Welcome to my first FastAPI CRUD Board"}
