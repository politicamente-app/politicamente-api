# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 14:15:29

from sqlalchemy.orm import Session
import uuid
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create(db: Session, user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def remove(db: Session, *, id: uuid.UUID) -> User | None:
    obj = db.query(User).get(id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj