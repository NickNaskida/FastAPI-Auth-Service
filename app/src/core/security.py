from typing import Optional, Any

from src.core.config import settings
from src.utils.jwt import generate_jwt_token


secret_key = settings.SECRET_KEY
access_lifetime = settings.ACCESS_TOKEN_EXPIRE


def create_access_token(
    identity: str,
    claims: Optional[dict[str, Any]] = None,
    headers: Optional[dict[str, Any]] = None
) -> str:
    return generate_jwt_token(
        identity=identity,
        token_type="access",
        secret=secret_key,
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
        secret=secret_key,
        lifetime=access_lifetime,
        claims=claims,
        headers=headers
    )
