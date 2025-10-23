from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pais(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True)
    codigo_iso = Column(String(3), nullable=False)
    nombre_pais = Column(String(50), nullable=False)
    nacionalidad = Column(String(60), nullable=True)
