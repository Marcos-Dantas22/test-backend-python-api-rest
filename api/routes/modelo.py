from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import Modelo
from schemas.modelo import ModeloCreate,ModeloUpdate, ModeloResponse
from docs.modelo_docs import (
    create_modelo_docs,
    list_modelos_docs,
    get_modelo_docs,
    update_modelo_docs,
    delete_modelo_docs,
)

router = APIRouter(prefix="/modelos", tags=["Modelos"])

@router.post("/", response_model=ModeloResponse, **create_modelo_docs)
def create_modelo(modelo: ModeloCreate, db: Session = Depends(get_db)):
    existe_modelo = db.query(Modelo).filter(Modelo.nome == modelo.nome).first()
    if existe_modelo:
        raise HTTPException(status_code=400, detail="Já existe um modelo com esse nome")
    
    db_modelo = Modelo(**modelo.dict())
    db.add(db_modelo)
    db.commit()
    db.refresh(db_modelo)
    return db_modelo

@router.get("/", response_model=list[ModeloResponse], **list_modelos_docs)
def list_modelos(db: Session = Depends(get_db)):
    return db.query(Modelo).all()

@router.get("/{modelo_id}", response_model=ModeloResponse, **get_modelo_docs)
def get_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).get(modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    return modelo

@router.put("/{modelo_id}", response_model=ModeloResponse, **update_modelo_docs)
def update_modelo(modelo_id: int, data: ModeloUpdate, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).get(modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    
    existe_modelo = (
        db.query(Modelo)
        .filter(Modelo.nome == data.nome, Modelo.id != modelo_id)
        .first()
    )
    if existe_modelo:
        raise HTTPException(status_code=400, detail="Já existe outro modelo com esse nome")
    
    for key, value in data.dict().items():
        setattr(modelo, key, value)
    db.commit()
    db.refresh(modelo)
    return modelo

@router.delete("/{modelo_id}", response_model=dict, **delete_modelo_docs)
def delete_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).get(modelo_id)
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    db.delete(modelo)
    db.commit()
    return {"message": "Modelo deletado"}
