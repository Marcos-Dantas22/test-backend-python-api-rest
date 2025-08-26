from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from routes import carro, modelo, marca

from sqlalchemy.orm import Session
from config.database import Base, engine
from models.models import Marca
from models.models import Modelo
from models.models import Carro
from docs.api_info import api_title, api_description, api_version, api_contact, api_servers

app = FastAPI(
    title=api_title,
    description=api_description,
    version=api_version,
    contact=api_contact,
    servers=api_servers
)

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
app.include_router(marca.router)
app.include_router(modelo.router)
app.include_router(carro.router)

# Função para popular dados de teste
def create_test_data(db: Session):
    # Marcas
    if not db.query(Marca).first():
        marca1 = Marca(nome_marca="Fiat")
        marca2 = Marca(nome_marca="Chevrolet")
        db.add_all([marca1, marca2])
        db.commit()
        db.refresh(marca1)
        db.refresh(marca2)

        # Modelos
        modelo1 = Modelo(marca_id=marca1.id, nome="Uno", valor_fipe=35000)
        modelo2 = Modelo(marca_id=marca2.id, nome="Onix", valor_fipe=60000)
        db.add_all([modelo1, modelo2])
        db.commit()
        db.refresh(modelo1)
        db.refresh(modelo2)

        # Carros
        carro1 = Carro(modelo_id=modelo1.id, ano=2020, combustivel="Flex", num_portas=4, cor="Vermelho")
        carro2 = Carro(modelo_id=modelo2.id, ano=2022, combustivel="Gasolina", num_portas=4, cor="Preto")
        db.add_all([carro1, carro2])
        db.commit()

# Inicializa dados de teste ao iniciar a API
@app.on_event("startup")
def startup_event():
    db = Session(bind=engine)
    create_test_data(db)
    db.close()