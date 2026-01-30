from fastapi import FastAPI
from app.db import database, models
from app.api import employees, auth

# Crear las tablas en la DB al iniciar
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="BioEntry-AI API")

# Incluir las rutas del CRUD
app.include_router(employees.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Bienvenido al Sistema de Identificación Facial BioEntry-AI"}