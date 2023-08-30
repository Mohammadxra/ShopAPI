from sqlalchemy.orm import Session
from db.models import Contact
import  datetime

def add_contact(
        name:str,
        email:str,
        subject:str,
        message:str,
        db:Session
):
    new_contact = Contact(
        name = name,
        email = email,
        date = datetime.datetime.now(),
        subject = subject,
        message = message,
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)