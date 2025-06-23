# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:30:17

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:32:04

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()