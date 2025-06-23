# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:36:49

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:38:15

import uuid
from pydantic import BaseModel, EmailStr, Field
from typing import List
from .vote import VoteResponse

class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, example="José da Silva")
    email: EmailStr = Field(..., example="jose.silva@email.com")
    password: str = Field(..., min_length=8, example="senhaSegura123")

class UserResponse(BaseModel):
    user_id: uuid.UUID
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class UserDataExport(BaseModel):
    """Schema para a exportação completa de dados do usuário."""
    profile: UserResponse
    votes: List[VoteResponse] = []

    class Config:
        from_attributes = True