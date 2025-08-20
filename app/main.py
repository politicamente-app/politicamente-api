# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 14:15:29

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app.db.base import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PoliticaMente API",
    description="Backend para a plataforma PoliticaMente.",
    version="1.0.0"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    # Adicione aqui os domínios do seu frontend em produção quando for o caso
    # Ex: "https://www.politicamente.com.br"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do PoliticaMente"}