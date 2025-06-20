from fastapi import FastAPI
from app.api.api import api_router
from app.db import base

# Cria todas as tabelas no banco de dados (se não existirem)
base.Base.metadata.create_all(bind=base.engine)

app = FastAPI(
    title="PoliticaMente API",
    description="Backend para a plataforma PoliticaMente.",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/", tags=["Root"])
def read_root():
    """Endpoint inicial para verificar se a API está no ar."""
    return {"message": "Bem-vindo à API do PoliticaMente"}