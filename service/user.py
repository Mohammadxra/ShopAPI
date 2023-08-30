from sqlalchemy.orm import Session
from db.models import User

def add(
    username: str, nickname: str, email: str, password: int, db: Session
):
    new_user = User(
        name=username,
        nickname=nickname,
        email = email,
        password=password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user