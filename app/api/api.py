# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:07:40

from fastapi import APIRouter
from app.api.endpoints import auth

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])