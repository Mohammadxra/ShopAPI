from fastapi import APIRouter , Depends , Response , Request
import os
from db.database import get_db
from sqlalchemy.orm import Session
from db.models import Category , Product
from router.user import templates
from service import category

router = APIRouter(
    tags=["Categories"]
)

@router.post("/post/cat")
def add_category(name:str, db:Session = Depends(get_db)):
    return category.create_category(name,db)

@router.post("/test/cookie")
def test():
    response = Response()
    response.set_cookie("MESSAGE","vhjhjnbgvhj")
    return response

@router.get("/category/{category_name}")
def category_products(category_name:str, request:Request, db:Session = Depends(get_db)):
    products = db.query(Product).filter(Product.category == category_name)
    listt = []
    for i in products:
        listt.append(i)
    if len(listt) == 0 :
        return templates.TemplateResponse("404.html", {"request":request})
    else:
        return templates.TemplateResponse("category.html", {"request":request,"products":products})