from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import Carro
from pydantic import BaseModel
from typing import Optional
from routes.modelo import ModeloResponse
from datetime import datetime

router = APIRouter(prefix="/carros", tags=["Carros"])

# Schemas
class CarroCreate(BaseModel):
    modelo_id: int
    ano: int
    combustivel: str
    num_portas: int
    cor: str

class CarroUpdate(BaseModel):
    modelo_id: int
    ano: int
    combustivel: str
    num_portas: int
    cor: str

class CarroResponse(BaseModel):
    id: int
    timestamp_cadastro: datetime
    modelo_id: int
    ano: int
    combustivel: str
    num_portas: int
    cor: str
    # opcional: incluir dados do modelo
    modelo: Optional[ModeloResponse] = None

    class Config:
        orm_mode = True
# CRUD
@router.post("/", response_model=dict)
def create_carro(carro: CarroCreate, db: Session = Depends(get_db)):
    db_carro = Carro(**carro.dict())
    db.add(db_carro)
    db.commit()
    db.refresh(db_carro)
    return db_carro.__dict__

@router.get("/", response_model=list[CarroResponse])
def list_carros(db: Session = Depends(get_db)):
    return db.query(Carro).all()

@router.get("/{carro_id}", response_model=CarroResponse)
def get_carro(carro_id: int, db: Session = Depends(get_db)):
    carro = db.query(Carro).get(carro_id)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return carro.__dict__

@router.put("/{carro_id}", response_model=dict)
def update_carro(carro_id: int, data: CarroUpdate, db: Session = Depends(get_db)):
    carro = db.query(Carro).get(carro_id)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    for key, value in data.dict().items():
        setattr(carro, key, value)
    db.commit()
    db.refresh(carro)
    return carro.__dict__

@router.delete("/{carro_id}", response_model=dict)
def delete_carro(carro_id: int, db: Session = Depends(get_db)):
    carro = db.query(Carro).get(carro_id)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    db.delete(carro)
    db.commit()
    return {"message": "Carro deletado"}
