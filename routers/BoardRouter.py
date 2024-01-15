from sqlalchemy.orm import Session
from db.connection import get_db

from fastapi import APIRouter

app = APIRouter(
    prefix="/board",
)


@app.get("/test")
async def board_test():
    return "test"
