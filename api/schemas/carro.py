
from pydantic import BaseModel
from typing import Optional
from api.routes.modelo import ModeloResponse
from datetime import datetime

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

    modelo: Optional[ModeloResponse] = None

    class Config:
        orm_mode = True