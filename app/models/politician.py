# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:07:40

import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base

class Politician(Base):
    __tablename__ = "politicians"
    politician_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String, index=True, nullable=False)
    nickname = Column(String)