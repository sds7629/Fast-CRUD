from sqlalchemy.orm import Session
from models.board_model import Board
from schema.board_schema import NewPost, PostList


def insert_post(new_post: NewPost, db: Session):
    post = Board(writer=new_post.writer, title=new_post.title, content=new_post.content)
    db.add(post)
    db.commit()

    return post.pk


def list_all_post(db: Session):
    lists = db.query(Board).filter(Board.del_yn == "Y").all()
    return [
        PostList(pk=row.pk, writer=row.writer, title=row.title, date=row.date)
        for row in lists
    ]
    # return lists
