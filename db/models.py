from db.database import Base
from sqlalchemy import String , Integer , Column , Float

class User(Base):
    __tablename__ = "users"
    name = Column(String)
    nickname = Column(String,primary_key=True)
    password = Column(Integer,primary_key=True)
    email = Column(String)


class Product(Base):
    __tablename__ = "products"
    _id = Column(Integer,primary_key=True,unique=True,index=True)
    price = Column(Float)
    name = Column(String)
    category = Column(String)
    gender = Column(String)
    detail = Column(String)
    image = Column(String)


class Category(Base):
    __tablename__ = "categories"
    _id = Column(Integer,primary_key=True,index=True)
    name = Column(String)


class Contact(Base):
    __tablename__= "contacts"
    slug = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    date = Column(String)
    message = Column(String)
    subject = Column(String)

    
