from time import time
from typing import Dict, Any, Union

import jwt
from pydantic import SecretStr

SecretType = Union[str, SecretStr]
JWT_ALGORITHM = "HS256"


def _get_secret(secret: SecretType) -> SecretType:
    """Get the secret key."""
    if isinstance(secret, SecretStr):
        return secret.get_secret_value()
    return secret


def generate_jwt_token(
        identity: str,
        token_type: str,
        secret: SecretType,
        lifetime: int,
        algorithm: str = JWT_ALGORITHM,
        claims: Dict[str, Any] = None,
        headers: Dict[str, Any] = None,
) -> str:
    """Generate a JWT token."""
    current_time = int(time())

    payload = {
        "iat": current_time,
        "sub": identity,
        "type": token_type,
        "nbf": current_time,
        "exp": current_time + lifetime
    }
    payload.update(claims or {})

    return jwt.encode(
        payload,
        _get_secret(secret),
        algorithm=algorithm,
        headers=headers
    )


def decode_jwt_token(
        jwt_token: str,
        secret: SecretType,
        algorithm: str = JWT_ALGORITHM
) -> Dict[str, Any]:
    """Decode a JWT token."""
    return jwt.decode(
        jwt_token,
        _get_secret(secret),
        algorithms=[algorithm]
    )
