from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db

router =APIRouter(prefix="/products",tags=["Product"])

@router.post("/",response_model=schemas.ProductResponse)
def create_product(product:schemas.ProductCreate,db:Session=Depends(get_db)):
    return crud.create_product(db,product)

@router.get("/",response_model=List[schemas.ProductResponse])
def list_product(skip: int=0,limit:int=50,db:Session=Depends(get_db)):
    return crud.get_products(db,skip=skip,limit=limit)

@router.get("/search",response_model=List[schemas.ProductResponse])
def search_product(
    q: str = Query(...,description="Search Query"),
    company_id: int = Query(None),
    skip: int=0,
    limit: int=50,
    db:Session=Depends(get_db)
):
    return crud.search_product(db,q,company_id,skip)
    
@router.get("/{product_id}",response_model=schemas.ProductResponse)
def get_product(product_id:int,db:Session=Depends(get_db)):
    return crud.get_product(db,product_id)