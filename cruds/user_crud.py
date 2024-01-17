from sqlalchemy.orm import Session
from models.user_model import User
from schema.user_schema import NewUserForm
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(email: str, db=Session):
    return db.query(User).filter(User.email == email).first()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_user(new_user: NewUserForm, db: Session):
    user = User(
        user_name=new_user.name,
        email=new_user.email,
        hashed_pw=pwd_context.hash(new_user.password),
    )
    db.add(user)
    db.commit()
