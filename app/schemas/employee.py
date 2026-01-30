from pydantic import BaseModel

class EmployeeBase(BaseModel):
    full_name: str
    employee_id: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    photo_path: str
    is_active: bool

    class Config:
        from_attributes = True