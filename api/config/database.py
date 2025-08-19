from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Pega a URL do banco do ambiente
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria engine
engine = create_engine(DATABASE_URL)

# Session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os models
Base = declarative_base()

# Dependência do banco (para usar nas rotas)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
