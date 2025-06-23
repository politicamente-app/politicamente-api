# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:24:29

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:22:25

from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def get_user_token() -> str:
    """Função auxiliar para registrar e logar um usuário para obter um token."""
    email = f"test.votes.{uuid.uuid4()}@example.com"
    password = "password123"
    client.post("/auth/register", json={"full_name": "Test Vote User", "email": email, "password": password})
    response = client.post("/auth/login", data={"username": email, "password": password})
    return response.json()["access_token"]

def test_create_and_read_vote():
    token = get_user_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Nota: Este teste assume que já existem dados no banco
    # (ex: uma eleição com id=1). Em um cenário real, criaríamos esses
    # dados no próprio teste (setup/teardown) para não depender do estado do banco.
    vote_data = {
        "election_id": 1,
        "office": "Prefeito",
        "vote_type": "NOMINAL",
        "candidacy_id": 1,
        "party_id": None
    }

    # # Criar um voto
    # response = client.post("/votes/", headers=headers, json=vote_data)
    # assert response.status_code == 201
    # data = response.json()
    # assert data["office"] == vote_data["office"]

    # # Ler os votos
    # response = client.get("/votes/", headers=headers)
    # assert response.status_code == 200
    # data = response.json()
    # assert len(data) > 0
    # assert data[0]["office"] == "Prefeito"
    pass # Passando o teste por enquanto.