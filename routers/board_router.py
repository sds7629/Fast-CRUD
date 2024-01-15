from sqlalchemy.orm import Session
from db.connection import get_db

from fastapi import APIRouter, Depends
from schema.board_schema import NewPost, PostList
from sqlalchemy.orm import Session
from db.connection import get_db
from cruds import board_crud

app = APIRouter(
    prefix="/board",
)


@app.post(path="/create", description="게시판 글 생성")
async def create_new_post(new_post: NewPost, db: Session = Depends(get_db)):
    return board_crud.insert_post(new_post, db)


@app.get(path="/read", description="게시글 조회")
async def read_all_post(db: Session = Depends(get_db)):
    return board_crud.list_all_post(db)
