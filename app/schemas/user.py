import uuid
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    """Schema para a criação de um usuário."""
    full_name: str = Field(..., min_length=3, example="José da Silva")
    email: EmailStr = Field(..., example="jose.silva@email.com")
    password: str = Field(..., min_length=8, example="senhaSegura123")

class UserResponse(BaseModel):
    """Schema para a resposta da API ao criar/obter um usuário."""
    user_id: uuid.UUID
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    """Schema para a resposta do token de acesso."""
    access_token: str
    token_type: str