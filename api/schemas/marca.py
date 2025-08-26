
from pydantic import BaseModel

class MarcaCreate(BaseModel):
    nome_marca: str

class MarcaUpdate(BaseModel):
    nome_marca: str

class MarcaResponse(BaseModel):
    id: int
    nome_marca: str

    class Config:
        orm_mode = True
