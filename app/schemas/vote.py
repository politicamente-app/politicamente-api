# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 13:50:04

import uuid
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class VoteTypeEnum(str, Enum):
    nominal = "NOMINAL"
    party = "PARTY"
    justified = "JUSTIFIED"
    blank = "BLANK"
    null = "NULL"

class VoteBase(BaseModel):
    election_id: int
    office: str
    vote_type: VoteTypeEnum
    candidacy_id: Optional[int] = None
    party_id: Optional[int] = None

class VoteCreate(VoteBase):
    pass

class VoteUpdate(VoteBase):
    pass

class VoteResponse(VoteBase):
    vote_id: int
    user_id: uuid.UUID

    class Config:
        from_attributes = True