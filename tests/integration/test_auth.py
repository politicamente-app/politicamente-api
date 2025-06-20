from fastapi.testclient import TestClient
from app.main import app
from app.repository import user as user_repository
from app.db.session import get_db
from sqlalchemy.orm import Session

# Nota: Para um projeto real, usaríamos um banco de dados de teste separado.
# Por enquanto, este teste irá interagir com o seu banco de dados de desenvolvimento.

client = TestClient(app)

def test_full_auth_flow():
    # 1. Registro
    email = "test.user.flow@example.com"
    password = "password123"
    response = client.post(
        "/auth/register",
        json={"full_name": "Test Flow User", "email": email, "password": password},
    )
    # Ignora se o usuário já existe de um teste anterior
    assert response.status_code in [201, 400]

    # 2. Login
    response = client.post(
        "/auth/login",
        data={"username": email, "password": password},
    )
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    access_token = token_data["access_token"]

    # 3. Acesso à Rota Protegida
    response = client.get(
        "/auth/users/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == email

def test_get_current_user_no_token():
    response = client.get("/auth/users/me")
    assert response.status_code == 401 # Unauthorized

def test_get_current_user_invalid_token():
    response = client.get(
        "/auth/users/me",
        headers={"Authorization": "Bearer tokeninvalido"},
    )
    assert response.status_code == 401 # Unauthorized