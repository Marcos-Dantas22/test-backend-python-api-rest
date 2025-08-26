from pydantic import BaseModel
from typing import Optional
from routes.marca import MarcaResponse

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
    marca: Optional[MarcaResponse] = None

    class Config:
        orm_mode = True
