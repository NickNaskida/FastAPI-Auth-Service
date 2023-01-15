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
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_file = os.path.join(BASE_DIR, 'envs/.env')


class TestSettings(DevelopmentSettings):
    ...


class ProductionSettings(DevelopmentSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str = str(5432)
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

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

    SQLALCHEMY_POOL_SIZE: int = 20
    SQLALCHEMY_POOL_RECYCLE: int = 1200
    SQLALCHEMY_POOL_TIMEOUT: int = 5
    SQLALCHEMY_MAX_OVERFLOW: int = 10

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_reset_on_return": 'commit',  # looks like postgres likes this more than rollback
        'pool_size': SQLALCHEMY_POOL_SIZE,
        'pool_recycle': SQLALCHEMY_POOL_RECYCLE,
        'pool_timeout': SQLALCHEMY_POOL_TIMEOUT,
        'max_overflow': SQLALCHEMY_MAX_OVERFLOW,
    }

    class Config:
        env_file = os.path.join(BASE_DIR, 'envs/.env.prod')


settings = DevelopmentSettings()
