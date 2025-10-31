from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas,crud
from app.database import get_db

router = APIRouter(prefix="/companies",tags=["Companies"])

@router.post("/",response_model=schemas.CompanyResponse)
def create_company(company:schemas.CompanyCreate,db:Session=Depends(get_db)):
    return crud.create_company(db,company)

@router.get("/",response_model=List[schemas.CompanyResponse])
def list_companies(skip:int=0,limit:int=50,db:Session=Depends(get_db)):
    return crud.get_companies(db,skip,limit)

@router.get("/{company_id}",response_model=schemas.CompanyResponse)
def get_company(company_id:int,db:Session=Depends(get_db)):
    return crud.get_company(db,company_id)