# Este arquivo é usado para inicializar o banco de dados e garantir
# que o SQLAlchemy conheça todos os nossos modelos e a engine.
from app.db.base_class import Base
from app.models.user import User
from app.db.session import engine