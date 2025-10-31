from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.database import db
from app.models import EmployeeCreate
from app.utils import validate_csv_columns, save_df_to_file
import pandas as pd
import os

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400,details="Only csv allowed")
    
    file_path = os.path.join(UPLOAD_DIR,file.filename)
    with open(file_path,"wb") as f:
        f.write(await file.read())
        
    df = pd.read_csv(file_path)
    required_cols = {"name","email","department","salary"}
    validate_csv_columns(df,required_cols)
    
    for _, row in df.iterrows():
        try:
            await db.employee.create(
                data={
                    "name": row["name"],
                    "email": row["email"],
                    "department": row.get("department",None),
                    "salary": float(row["salary"]) if not pd.isna(row["salary"]) else None
                }
            )
        except:
            continue
    return {"message": "csv uploaded successfully"}

@router.get("/download_data/")
async def download_data(format: str="csv",limit: int | None = None):
    data = await db.employee.find_many(take=limit)
    if not data:
        raise HTTPException(status_code=404,details="No Data Found")
    
    df = pd.DataFrame([d.model_dump() for d in data])
    file_name = f"employee.{format}"
    file_path = os.path.join(UPLOAD_DIR,file_name)
    save_df_to_file(df,file_path,format)
    return FileResponse(file_path,media_type="application/octet-stream",filename = file_name)

@router.post("/add_employee/")
async def add_employee(employee: EmployeeCreate):
    return await db.employee.create(data=employee.model_dump())
    
    