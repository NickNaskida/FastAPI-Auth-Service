import aioredis

from src.core.config import settings

redis_host = settings.REDIS_HOST
redis_db = settings.REDIS_DB
redis_username = settings.REDIS_USERNAME
redis_password = settings.REDIS_PASSWORD

redis = await aioredis.from_url("redis://localhost",  db=redis_db, password=redis_password, username=redis_username)
