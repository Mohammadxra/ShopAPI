from fastapi import APIRouter , Depends , Request , Form , status
from db.database import get_db
from sqlalchemy.orm import Session
from service import user
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from db.models import Product , Category
import db
router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/home")
def home(request: Request,db:Session = Depends(get_db)):
    products = db.query(Product).all()
    products = products[:6]
    categories = db.query(Category).all()
    return templates.TemplateResponse("home.html",{"request":request,"products":products,"categories":categories})

@router.get("/")
def signup(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@router.post("/add")
def add_user(
    username : str = Form("application/x-www-form-urlencode"),
    nickname : str = Form("application/x-www-form-urlencode"),
    email : str = Form("application/x-www-form-urlencode"),
    password : int = Form("application/x-www-form-urlencode"),
    db : Session = Depends(get_db)
):
    user.add(username,nickname,email,password,db)

    url = router.url_path_for('home')
    return RedirectResponse(url,status_code=status.HTTP_303_SEE_OTHER)