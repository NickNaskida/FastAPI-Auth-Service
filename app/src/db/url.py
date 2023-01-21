from src.core.config import settings


def get_sqlalchemy_url() -> str:
    """Get and build SQLAlchemy URL from settings."""
    p_user = settings.POSTGRES_USER
    p_password = settings.POSTGRES_PASSWORD
    p_server = settings.POSTGRES_SERVER
    p_db = settings.POSTGRES_DB
    p_port = settings.POSTGRES_PORT

    return f"postgresql+asyncpg://{p_user}:{p_password}@{p_server}:{p_port}/{p_db}"
