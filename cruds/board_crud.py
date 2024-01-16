from sqlalchemy.orm import Session
from sqlalchemy import and_
from models.board_model import Board
from schema.board_schema import NewPost, PostList, Post, UpdatePost


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


def get_post(post_pk: int, db: Session):
    try:
        post = db.query(Board).filter(Board.pk == post_pk, Board.del_yn == "Y").first()
        return Post(
            pk=post.pk,
            writer=post.writer,
            title=post.title,
            content=post.content,
            date=post.date,
        )
    except Exception as e:
        return {"error": str(e), "msg": "존재하지 않는 게시글데스"}


def update_post(update_post: UpdatePost, db: Session):
    post = (
        db.query(Board)
        .filter(and_(Board.pk == update_post.pk, Board.del_yn == "Y"))
        .first()
    )
    try:
        if not post:
            raise Exception("존재하지 않는 게시글입니다.")

        post.title = update_post.title
        post.content = update_post.content
        db.commit()
        db.refresh(post)
        return get_post(post.pk, db)

    except Exception as e:
        return str(e)


def del_post(post_pk: int, db: Session):
    post = (
        db.query(Board).filter(and_(Board.pk == post_pk, Board.del_yn == "Y")).first()
    )
    try:
        if not post:
            raise Exception("존재하지 않는 게시글")
        post.del_yn = "N"
        db.commit()
        db.refresh(post)
        return {"msg": "삭제되었습니다."}

    except Exception as e:
        return str(e)
