from typing import Optional, Any

from passlib.hash import pbkdf2_sha256

from src.core.config import settings
from src.utils.jwt import generate_jwt_token

access_lifetime = settings.ACCESS_TOKEN_EXPIRE
refresh_lifetime = settings.REFRESH_TOKEN_EXPIRE


def create_access_token(
    identity: str,
    claims: Optional[dict[str, Any]] = None,
    headers: Optional[dict[str, Any]] = None
) -> str:
    return generate_jwt_token(
        identity=identity,
        token_type="access",
        lifetime=access_lifetime,
        claims=claims,
        headers=headers
    )


def create_refresh_token(
    identity: str,
    claims: Optional[dict[str, Any]] = None,
    headers: Optional[dict[str, Any]] = None
) -> str:
    return generate_jwt_token(
        identity=identity,
        token_type="refresh",
        lifetime=refresh_lifetime,
        claims=claims,
        headers=headers
    )


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)
