from fastapi import APIRouter, HTTPException
from app.db import prisma
from pydantic import BaseModel

router = APIRouter(prefix="/products",tags=["Produts"])
db = prisma

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    companyId: int 
    categoryId: int | None = None
    
@router.post("/")
async def create_product(product: ProductCreate):
    existing = await db.product.find_first(where={"name":product.name,"companyId":product.companyId})
    if existing:
        raise HTTPException(status_code=404,detail="Product Already Exist")
    return await db.product.create(data=product.model_dump())

@router.get("/")
async def get_products():
    return await prisma.product.find_many(include={"company":True,"category":True})
    