from fastapi.testclient import TestClient
from app.main import app
import uuid

# Nota: Para um projeto real, usaríamos um banco de dados de teste separado.
# Por enquanto, este teste irá interagir com o seu banco de dados de desenvolvimento.

client = TestClient(app)

def test_full_auth_flow():
    # 1. Registro
    # Usamos um UUID para garantir que o e-mail seja único a cada execução do teste
    unique_email = f"test.user.flow.{uuid.uuid4()}@example.com"
    password = "password123"

    response = client.post(
        "/auth/register",
        json={"full_name": "Test Flow User", "email": unique_email, "password": password},
    )
    assert response.status_code == 201, response.text

    # 2. Login
    response = client.post(
        "/auth/login",
        data={"username": unique_email, "password": password},
    )
    assert response.status_code == 200, response.text
    token_data = response.json()
    assert "access_token" in token_data
    access_token = token_data["access_token"]

    # 3. Acesso à Rota Protegida
    response = client.get(
        "/auth/users/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    assert response.status_code == 200, response.text
    user_data = response.json()
    assert user_data["email"] == unique_email

def test_get_current_user_no_token():
    response = client.get("/auth/users/me")
    assert response.status_code == 401 # Unauthorized

def test_get_current_user_invalid_token():
    response = client.get(
        "/auth/users/me",
        headers={"Authorization": "Bearer tokeninvalido"},
    )
    assert response.status_code == 401 # Unauthorized