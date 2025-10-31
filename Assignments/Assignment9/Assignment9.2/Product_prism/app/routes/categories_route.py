from fastapi import APIRouter, HTTPException
from app.db import prisma
from pydantic import BaseModel

router = APIRouter(prefix="/categories", tags=["Categories"])
db = prisma

class CategoryCreate(BaseModel):
    name: str   
    
@router.post("/")
async def create_category(category: CategoryCreate):
    existing = await db.category.find_unique(where={"name":category.name})
    if existing:
        raise HTTPException(status_code=404,detail="Category Already Exist")
    return await db.category.create(data=category.model_dump())

@router.get("/")
async def get_categories():
    return await db.category.find_many()