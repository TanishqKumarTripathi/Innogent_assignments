from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name:str
    email:str
    department: str | None = None
    salary: float | None = None
    