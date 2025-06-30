# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 14:15:29

from sqlalchemy import Column, String, Integer, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base_class import Base

# Tabela de associação para a relação Muitos-para-Muitos entre Coligações e Partidos
coalition_parties_association = Table(
    'coalition_parties', Base.metadata,
    Column('coligacao_id', Integer, ForeignKey('coalitions.coligacao_id'), primary_key=True),
    Column('party_id', Integer, ForeignKey('parties.party_id'), primary_key=True)
)

class Coalition(Base):
    __tablename__ = "coalitions"
    coligacao_id = Column(Integer, primary_key=True, index=True)
    nome_coligacao = Column(String, nullable=False)
    id_eleicao_fk = Column(Integer, ForeignKey("elections.election_id"), nullable=False)

    election = relationship("Election")
    parties = relationship("Party", secondary=coalition_parties_association)

    __table_args__ = (
        UniqueConstraint('nome_coligacao', 'id_eleicao_fk', name='_nome_coligacao_eleicao_uc'),
    )