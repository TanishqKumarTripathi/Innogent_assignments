import pandas as pd
from fastapi import HTTPException 

def validate_csv_columns(df,required_cols):
    if not required_cols.issubset(df.columns):
        raise HTTPException(status_code=404,detail=f"CSV must have one columns: {required_cols}")
    
def save_df_to_file(df,file_path,format):
    if format == "csv":
        df.to_csv(file_path,index=False)
    elif format in ("xls","xlsx"):
        df.to_excel(file_path,index=False)
    else:
        raise HTTPException(status_code=400,detail="Supported format: csv, xls,xlsx")