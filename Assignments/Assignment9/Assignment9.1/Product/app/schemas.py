from pydantic import BaseModel
from typing import List,Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    company_id: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int 
    class Config:
        orm_model=True

class CompanyBase(BaseModel):
    name: str
    location: Optional[str] = None 
    
class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int
    product: List[ProductResponse] = []
    class Config:
        orm_model = True
        
class CategoryBase(BaseModel):
    name: str
    
class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int 
    products: List[ProductResponse]=[]
    class Config:
        orm_model = True
    