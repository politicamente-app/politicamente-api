# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:24:29

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:22:25

from sqlalchemy.orm import Session
from typing import List
import uuid

from app.models.vote import Vote
from app.schemas.vote import VoteCreate

def create_with_owner(db: Session, *, obj_in: VoteCreate, user_id: uuid.UUID) -> Vote:
    # O operador ** desempacota o dicionário do schema Pydantic nos argumentos do modelo SQLAlchemy
    db_obj = Vote(
        **obj_in.model_dump(),
        user_id=user_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_multi_by_owner(db: Session, *, user_id: uuid.UUID, skip: int = 0, limit: int = 100) -> List[Vote]:
    return (
        db.query(Vote)
        .filter(Vote.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )