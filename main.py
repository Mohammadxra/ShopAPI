from fastapi import FastAPI
from router import user , product , category , contact
from db.database import Base
from db import models
from db.database import engine
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(user.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(contact.router)
models.Base.metadata.create_all(bind=engine)