from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Company(Base):
    __tablename__ = "companies"
    id= Column(Integer,primary_key=True,index=True)
    name= Column(String,unique=True,nullable=False)
    location = Column(String)
    
    products = relationship("Product",back_populates="company")
    
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,unique=True,nullable=False)
    
    products = relationship("Product",back_populates="category")
    
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    description = Column(String)
    price = Column(Integer)
    company_id = Column(Integer,ForeignKey("companies.id"))
    category_id = Column(Integer,ForeignKey("categories.id"))
    
    company = relationship("Company",back_populates="products")
    category = relationship("Category",back_populates="products")
    