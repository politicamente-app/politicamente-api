# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-30 14:15:29

from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def get_user_token_for_votes(client: TestClient) -> str:
    """Função auxiliar para registrar e logar um usuário para obter um token."""
    email = f"test.votes.{uuid.uuid4()}@example.com"
    password = "password123"
    client.post("/auth/register", json={"full_name": "Test Vote User", "email": email, "password": password})
    response = client.post("/auth/login", data={"username": email, "password": password})
    return response.json()["access_token"]

def test_vote_crud_flow():
    pass