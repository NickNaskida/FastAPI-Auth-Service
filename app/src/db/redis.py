import aioredis
from aioredis import Redis

from src.core.config import settings

redis_host = settings.REDIS_HOST
redis_db = settings.REDIS_DB
redis_username = settings.REDIS_USERNAME
redis_password = settings.REDIS_PASSWORD


async def get_redis_client() -> Redis:
    redis = aioredis.from_url("redis://localhost",  db=redis_db)
    return redis
