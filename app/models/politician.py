# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-23 16:55:54

import uuid
from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base

class Politician(Base):
    __tablename__ = "politicians"

    politician_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String, index=True, nullable=False)
    nickname = Column(String)

    __table_args__ = (
        UniqueConstraint('full_name', 'nickname', name='_full_name_nickname_uc'),
    )