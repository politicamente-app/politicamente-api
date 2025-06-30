# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 13:50:04

from sqlalchemy import Column, String, Integer
from app.db.base_class import Base

class Party(Base):
    __tablename__ = "parties"
    party_id = Column(Integer, primary_key=True, index=True)
    party_name = Column(String, nullable=False)
    initials = Column(String, unique=True, index=True, nullable=False)
    party_number = Column(Integer, unique=True, nullable=False)