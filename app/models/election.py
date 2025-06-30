# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 13:29:06

from sqlalchemy import Column, String, Integer, Date
from app.db.base_class import Base

class Election(Base):
    __tablename__ = "elections"
    election_id = Column(Integer, primary_key=True, index=True)
    election_date = Column(Date, nullable=False)
    election_type = Column(String, nullable=False) # 'MUNICIPAL', 'GERAL'
    turn = Column(Integer, nullable=False) # 1 ou 2