from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import shutil
import os

from app.db import database, models
from app.core.face_logic import verify_faces

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/verify")
def verify_access(
    employee_id: str, 
    file: UploadFile = File(...), 
    db: Session = Depends(database.get_db)
):
    # Buscar al empleado en la DB
    employee = db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Empleado no registrado")

    # Guardar temporalmente la foto capturada en vivo
    temp_live_path = f"app/static/temp_{employee_id}.jpg"
    with open(temp_live_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Llamar al motor de IA para comparar
    comparison = verify_faces(employee.photo_path, temp_live_path)

    # Limpiar archivo temporal
    if os.path.exists(temp_live_path):
        os.remove(temp_live_path)

    if "error" in comparison:
        raise HTTPException(status_code=400, detail=comparison["error"])

    # Resultado de la validación
    is_match = comparison["verified"]
    
    if is_match:
        return {
            "access": "GRANTED",
            "employee": employee.full_name,
            "confidence": 1 - comparison["distance"]
        }
    else:
        return {"access": "DENIED", "reason": "Rostro no coincide con el carnet registrado"}