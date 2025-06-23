# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:30:17

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:32:04

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserResponse, Token
from app.repository import user as user_repository
from app.db.session import get_db
from app.core.security import verify_password, create_access_token, get_current_user
from app.models.user import User

router = APIRouter()

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar novo usuário"
)
def register_new_user(user_data: UserCreate, db: Session = Depends(get_db)):
    db_user = user_repository.get_by_email(db, email=user_data.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    new_user = user_repository.create(db=db, user=user_data)
    return new_user

@router.post(
    "/login",
    response_model=Token,
    summary="Login do usuário"
)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.get_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get(
    "/users/me",
    response_model=UserResponse,
    summary="Obter usuário atual"
)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.delete("/users/me", response_model=UserResponse, summary="Deletar conta do usuário")
def delete_current_user(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Deleta a conta e todos os dados do usuário autenticado.
    """
    deleted_user = user_repository.remove(db=db, id=current_user.user_id)
    return deleted_user