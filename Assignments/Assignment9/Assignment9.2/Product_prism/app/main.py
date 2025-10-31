from fastapi import FastAPI
from prisma import Prisma
from contextlib import asynccontextmanager
from app.routes import company_routes, product_route, categories_route
from app.db import prisma

# prisma = Prisma()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Connecting to Prisma...")
    await prisma.connect()
    yield
    print("🛑 Disconnecting Prisma...")
    await prisma.disconnect()



app = FastAPI(
    title="Product Management API (Prisma ORM)",
    lifespan=lifespan
)

app.include_router(company_routes.router, prefix="/companies", tags=["Companies"])
app.include_router(product_route.router, prefix="/products", tags=["Products"])
app.include_router(categories_route.router, prefix="/categories", tags=["Categories"])
