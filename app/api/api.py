# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 14:15:29

from fastapi import APIRouter
from app.api.endpoints import auth, votes

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(votes.router, prefix="/votes", tags=["Votes"])