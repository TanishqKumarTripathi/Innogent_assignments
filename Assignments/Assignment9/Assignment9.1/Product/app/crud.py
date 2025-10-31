from sqlalchemy import String
from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def create_company(db: Session, company: schemas.CompanyCreate):
    existing = db.query(models.Company).filter(models.Company.name==company.name).first()
    if existing:
        raise HTTPException(status_code=400,detail="Company already exists")
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def get_company(db: Session,company_id:int):
    return db.query(models.Company).filter(models.Company.id==company_id).first()

def get_companies(db:Session,skip: int=0,limit:int=100):
    return db.query(models.Company).offset(skip).limit(limit).all()

def create_product(db: Session,product: schemas.ProductCreate):
    existing = db.query(models.Product).filter(models.Product.name == product.name,models.Product.company_id== product.company_id).first()
    if existing:
        raise HTTPException(status_code=400,detail="Product Already exist")
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session,product_id:int):
    product = db.query(models.Product).filter(models.Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404,details="Product doesn't exist")
    return product

def get_products(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def search_product(db:Session,q:str,company_id:int=None,skip:int=0,limit:int=50):
    query = db.query(models.Product)
    if q:
        query = query.filter(
            (models.Product.name.ilike(f"%{q}%"))|
            (models.Product.description.ilike(f"%{q}%"))|
            (models.Product.price.cast(String).ilike(f"%{q}%"))
        )
    if company_id:
        query = query.filter(models.Product.company_id==company_id)
    return query.offset(skip).limit(limit).all()

def create_categories(db:Session,category:schemas.CategoryCreate):
    existing = db.query(models.Category).filter(models.Category.name==category.name).first()
    if existing:
        raise HTTPException(status_code=400,details="Cateory already exist")
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db:Session,category_id:int):
    return db.query(models.Category).filter(models.Category.id==category_id).first()

def get_categories(db:Session,skip:int=0,limit:int=50):
    return db.query(models.Category).offset(skip).limit(limit).all()


    