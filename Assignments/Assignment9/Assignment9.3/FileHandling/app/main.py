from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import employee
from app.database import connect_db, disconnect_db

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await disconnect_db()
    
app =FastAPI(lifespan=lifespan)

app.include_router(employee.router,prefix="/employee",tags=["Employee"])