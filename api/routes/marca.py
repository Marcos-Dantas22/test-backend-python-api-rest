from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import Marca
from pydantic import BaseModel

router = APIRouter(prefix="/marcas", tags=["Marcas"])

# Schemas
class MarcaCreate(BaseModel):
    nome_marca: str

class MarcaUpdate(BaseModel):
    nome_marca: str

class MarcaResponse(BaseModel):
    id: int
    nome_marca: str

    class Config:
        orm_mode = True
        
# CRUD
@router.post("/", response_model=dict)
def create_marca(marca: MarcaCreate, db: Session = Depends(get_db)):
    db_marca = Marca(nome_marca=marca.nome_marca)
    db.add(db_marca)
    db.commit()
    db.refresh(db_marca)
    return {"id": db_marca.id, "nome_marca": db_marca.nome_marca}

@router.get("/", response_model=list[MarcaResponse])
def list_marcas(db: Session = Depends(get_db)):
    return db.query(Marca).all()

@router.get("/{marca_id}", response_model=MarcaResponse)
def get_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).get(marca_id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    return {"id": marca.id, "nome_marca": marca.nome_marca}

@router.put("/{marca_id}", response_model=dict)
def update_marca(marca_id: int, data: MarcaUpdate, db: Session = Depends(get_db)):
    marca = db.query(Marca).get(marca_id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    marca.nome_marca = data.nome_marca
    db.commit()
    db.refresh(marca)
    return {"id": marca.id, "nome_marca": marca.nome_marca}

@router.delete("/{marca_id}", response_model=dict)
def delete_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).get(marca_id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    db.delete(marca)
    db.commit()
    return {"message": "Marca deletada"}
