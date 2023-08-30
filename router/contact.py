from fastapi import APIRouter, Depends , Request , Form, status
import os
from .user import templates
from db.database import get_db
from sqlalchemy.orm import Session
from service import contact
from db.models import Contact
import datetime
from starlette.responses import RedirectResponse

router = APIRouter(
    tags=["contact"]
)

@router.get("/contact")
def contact_page(request:Request, db:Session = Depends(get_db)):
    return templates.TemplateResponse("contact.html",{"request":request})

@router.post("/contact_create")
def get_newcontact(db:Session = Depends(get_db),
    name : str = Form(media_type="application/x-www-form-urlencode"),
    email : str = Form(media_type="application/x-www-form-urlencode"),
    subject : str = Form(media_type="application/x-www-form-urlencode"),
    message : str = Form(media_type="application/x-www-form-urlencode"),
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
    url = router.url_path_for('contact_page')
    return RedirectResponse(url,status_code=status.HTTP_303_SEE_OTHER)