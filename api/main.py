from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from routes import carro, modelo, marca

from sqlalchemy.orm import Session
from config.database import Base, engine, get_db
from models.models import Marca
from models.models import Modelo
from models.models import Carro

app = FastAPI(title="API de Carros")

# Cria tabelas
Base.metadata.create_all(bind=engine)

# Configuração CORS
origins = [
    "*"  # permite todas as origens, ou substitua por ["http://localhost:3000"] para apenas front específico
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adiciona routers
