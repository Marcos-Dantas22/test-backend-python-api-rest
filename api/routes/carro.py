from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.config.database import get_db
from api.models.models import Carro, Modelo
from api.schemas.carro import CarroCreate, CarroResponse, CarroUpdate
from api.docs.carro_docs import (
    create_carro_docs,
    list_carros_docs,
    get_carro_docs,
    update_carro_docs,
    delete_carro_docs,
)

router = APIRouter(prefix="/carros", tags=["Carros"])

@router.post("/", response_model=CarroResponse,  **create_carro_docs)
def create_carro(carro: CarroCreate, db: Session = Depends(get_db)):
    existe_modelo = db.query(Modelo).filter(Modelo.id == carro.modelo_id).first()
    if not existe_modelo:
        raise HTTPException(status_code=400, detail="Modelo não encontrado")

    db_carro = Carro(**carro.dict())
    db.add(db_carro)
    db.commit()
    db.refresh(db_carro)
    return db_carro

@router.get("/", response_model=list[CarroResponse], **list_carros_docs)
def list_carros(db: Session = Depends(get_db)):
    return db.query(Carro).all()

@router.get("/{carro_id}", response_model=CarroResponse, **get_carro_docs)
def get_carro(carro_id: int, db: Session = Depends(get_db)):
    carro = db.query(Carro).get(carro_id)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return carro

@router.put("/{carro_id}", response_model=CarroResponse, **update_carro_docs)
def update_carro(carro_id: int, data: CarroUpdate, db: Session = Depends(get_db)):
    carro = db.query(Carro).get(carro_id)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    
    if data.modelo_id is not None:
        existe_modelo = db.query(Modelo).filter(Modelo.id == data.modelo_id).first()
        if not existe_modelo:
            raise HTTPException(status_code=400, detail="Modelo não encontrado")
        
    for key, value in data.dict().items():
        setattr(carro, key, value)
    db.commit()
    db.refresh(carro)
    return carro

@router.delete("/{carro_id}", response_model=dict, **delete_carro_docs)
def delete_carro(carro_id: int, db: Session = Depends(get_db)):
    carro = db.query(Carro).get(carro_id)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    db.delete(carro)
    db.commit()
    return {"message": "Carro deletado"}
