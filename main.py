from fastapi import FastAPI
from models import board_model
from db.connection import engine
from routers import board_router as b_router


board_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(b_router.app, tags=["board"])


@app.get("/")
def root():
    return {"Welcome to my first FastAPI CRUD Board"}
