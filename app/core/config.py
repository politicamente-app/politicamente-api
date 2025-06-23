# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:27:01

# Este arquivo foi gerado/atualizado pelo DomTech Forger em 2025-06-22 23:29:13

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()