from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from config.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nome_marca = Column(String, nullable=False, unique=True)



class Modelo(Base):
    __tablename__ = "modelos"

    id = Column(Integer, primary_key=True, index=True)
    marca_id = Column(Integer, ForeignKey("marcas.id"), nullable=False)
    nome = Column(String, nullable=False)
    valor_fipe = Column(Float, nullable=False)

    marca = relationship("Marca", backref="modelos")


class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    timestamp_cadastro = Column(DateTime, default=datetime.utcnow, nullable=False)
    modelo_id = Column(Integer, ForeignKey("modelos.id"), nullable=False)
    ano = Column(Integer, nullable=False)
    combustivel = Column(String, nullable=False)
    num_portas = Column(Integer, nullable=False)
    cor = Column(String, nullable=False)

    modelo = relationship("Modelo", backref="carros")