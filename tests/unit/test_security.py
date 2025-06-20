from app.core.security import get_password_hash, verify_password

def test_password_hashing():
    """
    Testa se o hashing e a verificação da senha funcionam corretamente.
    """
    password = "senhaSegura123"

    hashed_password = get_password_hash(password)

    assert password != hashed_password
    assert verify_password(password, hashed_password) == True
    assert verify_password("senhaIncorreta", hashed_password) == False