from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas,crud
from app.database import get_db

router = APIRouter(prefix="/categories",tags=["Categories"])

@router.post("/",response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate,db: Session=Depends(get_db)):
    return crud.create_categories(db,category)

@router.get("/",response_model=List[schemas.CategoryResponse])
def list_categories(skip:int=0,limit:int=50,db: Session=Depends(get_db)):
    return crud.get_categories(db,skip,limit)

@router.get("/{category_id}",response_model=schemas.CategoryResponse)
def get_category(category_id:int,db:Session=Depends(get_db)):
    category = crud.get_category(db,category_id)
    
    if not category:
        raise HTTPException(status_code=404,detail="Category not found!!!")
    return category
