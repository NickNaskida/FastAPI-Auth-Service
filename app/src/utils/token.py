from typing import Optional

from aioredis import Redis

from src.utils.jwt import decode_jwt_token
from src.models.user import User


async def add_refresh_token_to_redis(
    redis_client: Redis,
    user: User,
    refresh_token: str,
    ip: str,
    user_agent: str,
    fingerprint: str
) -> None:
    """
    Add refresh token to redis with other session information

    :param user: User model instance
    :param refresh_token: JWT token
    :param ip: IP address
    :param user_agent: User agent
    :param fingerprint: Fingerprint
    :param redis_client: Redis client
    :return: None
    """
    decoded_token = decode_jwt_token(refresh_token)
    session_id = decoded_token["jti"]

    mapping = {
        "refresh_token_id": session_id,
        "ip": ip,
        "user_agent": user_agent,
        "fingerprint": fingerprint,
        "exp": decoded_token["exp"],
        "created_at": decoded_token["iat"],
    }

    await redis_client.sadd(f"user:{user.id}", session_id)
    await redis_client.hset(f"user:{user.id}:{session_id}", mapping=mapping)


async def delete_token(redis_client: Redis, user: User):
    """
    Delete refresh token from redis.

    :param redis_client:
    :param user:
    :return:
    """
    pass
