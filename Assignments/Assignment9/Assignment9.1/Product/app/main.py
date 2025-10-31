from fastapi import FastAPI
from app.routes import product,company, categories
from app.database import Base,engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Managment API")

app.include_router(product.router)
app.include_router(company.router)
app.include_router(categories.router)