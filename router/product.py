from fastapi import APIRouter , File , UploadFile , Depends , Request
import os
from .user import templates
from db.database import get_db
from sqlalchemy.orm import Session
from service import product
from db.models import Product

router = APIRouter(
    tags=["product"]
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Mbase = BASE_DIR.split("\\")
splited = Mbase[ 0:len(Mbase) - 1 ]
Joined = "\\".join(splited)
UPLOAD_FILE = os.path.join(Joined, "static")


@router.post("/create",tags=["user"])
def create_product(
    price:float,
    name:str,
    category:str,
    gender:str,
    detail:str,
    file:UploadFile,
    post_number: int,
    db:Session = Depends(get_db)
):
    new_filename = "{0}{1}.png".format("pic",post_number)
    SAVE_FILE_PATH = os.path.join(UPLOAD_FILE,new_filename)
    with open(SAVE_FILE_PATH,"wb") as f:
        f.write(file.file.read())


    return product.add_product(
           price,
           name,
           category,
           gender,
           detail,
           SAVE_FILE_PATH,
           db
        )


@router.delete("/delete",tags=["user"])
def delete(request: Request, product_name:str, db:Session = Depends(get_db)):
    product= db.query(Product).delete(Product.name == product_name)
    return templates.TemplateResponse("home.html",{"request":request, "product":product})


@router.get("/product/{product_name}")
def retrieve_product(request: Request, product_name:str, db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.name == product_name).first()
    return templates.TemplateResponse("product.html",{"request":request, "product":product})


@router.get("/Store")
def store_product(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return templates.TemplateResponse("store.html",{"request":request, "products":products})