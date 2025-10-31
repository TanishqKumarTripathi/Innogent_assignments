from fastapi import APIRouter, HTTPException
from app.db import prisma
from pydantic import BaseModel

router = APIRouter(prefix="/companies",tags=["Companies"])
db = prisma

class CompanyCreate(BaseModel):
    name: str
    
@router.post("/")
async def create_company(company:CompanyCreate):
    existing = await db.company.find_unique(where={"name":company.name})
    if existing:
        raise HTTPException(status_code=400,detail="Company Already Exist")
    new_company = await db.company.create(data=company.model_dump())
    return new_company

@router.get("/")
async def get_companies():
    return await db.company.find_many()

@router.get("/{company_id}")
async def get_company(company_id:int):
    company = await db.company.find_unique(where={"id":company_id})
    if not company:
        raise HTTPException(status_code=404,detail="Company not found")
    return company
    