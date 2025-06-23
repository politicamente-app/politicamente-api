# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:36:49

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:32:04

from sqlalchemy.orm import Session
from typing import List, Any, Dict, Union
import uuid

from app.models.vote import Vote
from app.schemas.vote import VoteCreate, VoteUpdate

def get(db: Session, id: Any) -> Vote | None:
    return db.query(Vote).filter(Vote.vote_id == id).first()

def get_multi_by_owner(db: Session, *, user_id: uuid.UUID, skip: int = 0, limit: int = 100) -> List[Vote]:
    return (
        db.query(Vote)
        .filter(Vote.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def create_with_owner(db: Session, *, obj_in: VoteCreate, user_id: uuid.UUID) -> Vote:
    db_obj = Vote(**obj_in.model_dump(), user_id=user_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, *, db_obj: Vote, obj_in: Union[VoteUpdate, Dict[str, Any]]) -> Vote:
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True)

    for field in update_data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, update_data[field])

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove(db: Session, *, id: int) -> Vote | None:
    obj = db.query(Vote).get(id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj