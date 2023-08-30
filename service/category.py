from sqlalchemy.orm import Session
from db.models import Category


def create_category(name:str, db:Session):
    new_cat = Category(
        name = name
    )
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat