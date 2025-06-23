# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:30:17

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:32:04

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Any

from app.db.session import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.vote import VoteCreate, VoteUpdate, VoteResponse
from app.repository import vote as vote_repository

router = APIRouter()

@router.post("/", response_model=VoteResponse, status_code=status.HTTP_201_CREATED, summary="Registrar um novo voto")
def create_vote(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    vote_in: VoteCreate
) -> Any:
    """
    Cria um novo registro de voto para o usuário autenticado.
    """
    vote = vote_repository.create_with_owner(db=db, obj_in=vote_in, user_id=current_user.user_id)
    return vote

@router.get("/", response_model=List[VoteResponse], summary="Listar votos do usuário")
def read_votes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retorna uma lista de votos para o usuário autenticado.
    """
    votes = vote_repository.get_multi_by_owner(
        db=db, user_id=current_user.user_id, skip=skip, limit=limit
    )
    return votes

@router.put("/{vote_id}", response_model=VoteResponse, summary="Atualizar um voto")
def update_vote(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    vote_id: int,
    vote_in: VoteUpdate
) -> Any:
    """
    Atualiza um registro de voto existente.
    """
    vote = vote_repository.get(db=db, id=vote_id)
    if not vote:
        raise HTTPException(status_code=404, detail="Vote not found")
    if vote.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    updated_vote = vote_repository.update(db=db, db_obj=vote, obj_in=vote_in)
    return updated_vote

@router.delete("/{vote_id}", response_model=VoteResponse, summary="Deletar um voto")
def delete_vote(
    *,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    vote_id: int
) -> Any:
    """
    Deleta um registro de voto.
    """
    vote = vote_repository.get(db=db, id=vote_id)
    if not vote:
        raise HTTPException(status_code=404, detail="Vote not found")
    if vote.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    deleted_vote = vote_repository.remove(db=db, id=vote_id)
    return deleted_vote