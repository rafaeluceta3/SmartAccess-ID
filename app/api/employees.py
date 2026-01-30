from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import shutil
import os

from app.db import models, database
from app.schemas import employee as schemas

router = APIRouter(prefix="/employees", tags=["Employees"])

# 1. Crear Empleado (Create) con Foto de Carnet
@router.post("/", response_model=schemas.EmployeeResponse)
def create_employee(
    full_name: str, 
    employee_id: str, 
    file: UploadFile = File(...), 
    db: Session = Depends(database.get_db)
):
    # Guardar la foto físicamente
    file_location = f"app/static/{employee_id}_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    db_employee = models.Employee(
        full_name=full_name, 
        employee_id=employee_id, 
        photo_path=file_location
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# 2. Leer todos los empleados (Read)
@router.get("/", response_model=List[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(database.get_db)):
    return db.query(models.Employee).all()

# 3. Leer un empleado por ID
@router.get("/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(emp_id: str, db: Session = Depends(database.get_db)):
    employee = db.query(models.Employee).filter(models.Employee.employee_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return employee

# 4. Eliminar Empleado (Delete)
@router.delete("/{emp_id}")
def delete_employee(emp_id: str, db: Session = Depends(database.get_db)):
    employee = db.query(models.Employee).filter(models.Employee.employee_id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    db.delete(employee)
    db.commit()
    return {"message": "Empleado eliminado correctamente"}