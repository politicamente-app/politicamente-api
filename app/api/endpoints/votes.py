# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:24:29

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:22:25

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.vote import VoteCreate, VoteResponse
from app.repository import vote as vote_repository

router = APIRouter()

@router.post("/", response_model=VoteResponse, status_code=status.HTTP_201_CREATED, summary="Registrar um novo voto")
def create_vote(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    vote_in: VoteCreate
):
    """
    Cria um novo registro de voto para o usuário autenticado.
    """
    # A lógica para validar se a candidatura ou partido existem seria adicionada aqui
    vote = vote_repository.create_with_owner(db=db, obj_in=vote_in, user_id=current_user.user_id)
    return vote

@router.get("/", response_model=List[VoteResponse], summary="Listar votos do usuário")
def read_votes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
):
    """
    Retorna uma lista de votos para o usuário autenticado.
    """
    votes = vote_repository.get_multi_by_owner(
        db=db, user_id=current_user.user_id, skip=skip, limit=limit
    )
    return votes