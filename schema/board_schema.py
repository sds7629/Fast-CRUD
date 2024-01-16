from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NewPost(BaseModel):
    writer: str
    title: str
    content: str


class PostList(BaseModel):
    pk: int
    writer: str
    title: str
    date: datetime


class Post(BaseModel):
    pk: int
    writer: str
    title: str
    content: str
    date: datetime


class UpdatePost(BaseModel):
    pk: int
    title: str
    content: Optional[str] = None
