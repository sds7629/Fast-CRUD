from sqlalchemy.orm import Session
from db.connection import get_db
from typing import Optional
from fastapi import APIRouter, Depends
from schema.board_schema import NewPost, PostList, Post, UpdatePost
from sqlalchemy.orm import Session
from db.connection import get_db
from cruds import board_crud

app = APIRouter(
    prefix="/board",
)


# test
@app.post(path="/create", description="게시판 글 생성")
async def create_new_post(new_post: NewPost, db: Session = Depends(get_db)):
    return board_crud.insert_post(new_post, db)


@app.get(path="/read", description="게시글 조회", response_model=PostList)
async def read_all_post(db: Session = Depends(get_db), q: Optional[str] = None):
    if q:
        lists = board_crud.list_all_post(db)
        return lists[q]
    return board_crud.list_all_post(db)


@app.get(path="/read/{post_pk}", description="게시글 선택 조회", response_model=Post)
async def read_post(post_pk: int, db: Session = Depends(get_db)):
    return board_crud.get_post(post_pk, db)


@app.put(path="/update/{post_pk}", description="게시글 수정")
async def update_post(update_post: UpdatePost, db: Session = Depends(get_db)):
    return board_crud.update_post(update_post, db)


@app.delete(path="/delete/{post_pk}", description="게시글 삭제")
async def delete_post(post_pk: int, db: Session = Depends(get_db)):
    return board_crud.del_post(post_pk, db)
