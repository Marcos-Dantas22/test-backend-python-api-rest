from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import Marca
from schemas.marca import MarcaCreate, MarcaResponse, MarcaUpdate
from docs.marca_docs import (
    create_marca_docs,
    list_marcas_docs,
    get_marca_docs,
    update_marca_docs,
    delete_marca_docs,
)

router = APIRouter(prefix="/marcas", tags=["Marcas"])
        
@router.post("/", response_model=MarcaResponse, **create_marca_docs)
def create_marca(marca: MarcaCreate, db: Session = Depends(get_db)):
    existe_marca = db.query(Marca).filter(Marca.nome_marca == marca.nome_marca).first()
    if existe_marca:
        raise HTTPException(status_code=400, detail="Já existe uma marca com esse nome")
    
    db_marca = Marca(nome_marca=marca.nome_marca)
    db.add(db_marca)
    db.commit()
    db.refresh(db_marca)
    return {"id": db_marca.id, "nome_marca": db_marca.nome_marca}

@router.get("/", response_model=list[MarcaResponse], **list_marcas_docs)
def list_marcas(db: Session = Depends(get_db)):
    return db.query(Marca).all()

@router.get("/{marca_id}", response_model=MarcaResponse, **get_marca_docs)
def get_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).get(marca_id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    return {"id": marca.id, "nome_marca": marca.nome_marca}

@router.put("/{marca_id}", response_model=MarcaResponse, **update_marca_docs)
def update_marca(marca_id: int, data: MarcaUpdate, db: Session = Depends(get_db)):
    marca = db.query(Marca).get(marca_id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    
    # Verificar se o novo nome já existe em outra marca
    existe_marca = (
        db.query(Marca)
        .filter(Marca.nome_marca == data.nome_marca, Marca.id != marca_id)
        .first()
    )
    if existe_marca:
        raise HTTPException(status_code=400, detail="Já existe outra marca com esse nome")
    
    marca.nome_marca = data.nome_marca
    db.commit()
    db.refresh(marca)
    return {"id": marca.id, "nome_marca": marca.nome_marca}

@router.delete("/{marca_id}", response_model=dict, **delete_marca_docs)
def delete_marca(marca_id: int, db: Session = Depends(get_db)):
    marca = db.query(Marca).get(marca_id)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    db.delete(marca)
    db.commit()
    return {"message": f"Marca {marca.nome_marca} deletada"}


