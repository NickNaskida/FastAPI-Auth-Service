import os
import secrets
from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DevelopmentSettings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    PROJECT_NAME: str
    PROJECT_VERSION: str

    # JWT
    JWT_SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE: int = 60 * 15
    REFRESH_TOKEN_EXPIRE: int = 60 * 60 * 24 * 30

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_DB: int = 1
    REDIS_USERNAME: Optional[str] = None
    REDIS_PASSWORD: Optional[str] = None

    # Postgres
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str = str(5432)
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    # SQLAlchemy
    SQLALCHEMY_POOL_SIZE: int = 20
    SQLALCHEMY_POOL_RECYCLE: int = 1200
    SQLALCHEMY_POOL_TIMEOUT: int = 5
    SQLALCHEMY_MAX_OVERFLOW: int = 10

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER") + ":" + values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        env_file = os.path.join(BASE_DIR, 'envs/.env')


class TestSettings(DevelopmentSettings):
    ...


class ProductionSettings(DevelopmentSettings):

    class Config:
        env_file = os.path.join(BASE_DIR, 'envs/.env.prod')


settings = DevelopmentSettings()
