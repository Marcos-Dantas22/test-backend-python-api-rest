from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import Modelo
from pydantic import BaseModel
from typing import Optional
from routes.marca import MarcaResponse

router = APIRouter(prefix="/modelos", tags=["Modelos"])

# Schemas
class ModeloCreate(BaseModel):
    marca_id: int
    nome: str
    valor_fipe: float

class ModeloUpdate(BaseModel):
    marca_id: int
    nome: str
    valor_fipe: float

class ModeloResponse(BaseModel):
    id: int
    marca_id: int
    nome: str
    valor_fipe: float
    # opcional: incluir dados da marca
    marca: Optional[MarcaResponse] = None

    class Config:
        orm_mode = True

# CRUD
@router.post("/", response_model=dict)
def create_modelo(modelo: ModeloCreate, db: Session = Depends(get_db)):
    db_modelo = Modelo(**modelo.dict())
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo.__dict__

@router.get("/", response_model=list[ModeloResponse])
def list_modelos(db: Session = Depends(get_db)):
    return db.query(Modelo).all()

@router.get("/{modelo_id}", response_model=ModeloResponse)
def get_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).get(modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    return modelo.__dict__

@router.put("/{modelo_id}", response_model=dict)
def update_modelo(modelo_id: int, data: ModeloUpdate, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).get(modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    for key, value in data.dict().items():
        setattr(modelo, key, value)
    db.commit()
    db.refresh(modelo)
    return modelo.__dict__

@router.delete("/{modelo_id}", response_model=dict)
def delete_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).get(modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    db.delete(modelo)
    db.commit()
    return {"message": "Modelo deletado"}
