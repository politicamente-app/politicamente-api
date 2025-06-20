from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def get_by_email(db: Session, email: str) -> User | None:
    """Busca um usuário pelo seu e-mail."""
    return db.query(User).filter(User.email == email).first()

def create(db: Session, user: UserCreate) -> User:
    """Cria um novo usuário no banco de dados."""
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