# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-23 16:55:54

from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def get_user_token(client: TestClient) -> dict:
    """Função auxiliar para registrar e logar um usuário para obter um token."""
    email = f"test.auth.flow.{uuid.uuid4()}@example.com"
    password = "password123"

    client.post("/auth/register", json={"full_name": "Test Auth User", "email": email, "password": password})
    response = client.post("/auth/login", data={"username": email, "password": password})

    token_data = response.json()
    return {"token": token_data["access_token"], "email": email}


def test_full_auth_flow():
    auth_data = get_user_token(client)
    token = auth_data["token"]
    email = auth_data["email"]

    response = client.get(
        "/auth/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()
    assert user_data["email"] == email

def test_delete_user():
    auth_data = get_user_token(client)
    token = auth_data["token"]
    email = auth_data["email"]

    # Deleta o usuário
    response_delete = client.delete(
        "/auth/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response_delete.status_code == 200
    assert response_delete.json()["email"] == email

    # Tenta fazer login novamente (deve falhar)
    response_login_fail = client.post(
        "/auth/login",
        data={"username": email, "password": "password123"},
    )
    assert response_login_fail.status_code == 401

def test_export_user_data():
    auth_data = get_user_token(client)
    token = auth_data["token"]
    email = auth_data["email"]

    headers = {"Authorization": f"Bearer {token}"}

    # Exporta os dados
    response_export = client.get("/auth/users/me/data", headers=headers)
    assert response_export.status_code == 200

    data = response_export.json()
    assert data["profile"]["email"] == email
    assert "votes" in data