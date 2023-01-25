from fastapi import APIRouter, HTTPException, Request, Depends, status
from starlette_context import context
from aioredis import Redis

from src import crud
from src.schemas.token import Token
from src.utils.token import add_refresh_token_to_redis
from src.schemas.auth import RegisterPayload
from src.schemas.response import IPostResponseBase, create_response
from src.core.security import create_access_token, create_refresh_token
from src.db.redis import get_redis_client


router = APIRouter()

# TODO: Reverse proxy header setup (ip, user-agent, etc)


@router.post('/login')
async def login(request: Request):
    """Login user and create JWT access and refresh tokens"""
    pass


@router.post('/register')
async def register(
    request: RegisterPayload,
    redis_client: Redis = Depends(get_redis_client),
) -> IPostResponseBase[Token]:
    """Register user and create JWT access and refresh tokens"""

    # Get and check required headers
    # forwarded_for = context.data.get('X-Forwarded-For')   TODO: Figure out why this returns None
    forwarded_for = '000.000.00.00'
    user_agent = context.data.get('User-Agent')

    if not forwarded_for:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Missing X-Forwarded-For header')
    elif not user_agent:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Missing User-Agent header')

    # Validate username and email are unique
    user_exists = await crud.user.email_or_username_exists(email=request.email, username=request.username)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username or email already exists')

    # Create user
    user = await crud.user.create(obj_in=request)

    # Create tokens
    access_token = create_access_token(user.username)
    refresh_token = create_refresh_token(user.username)

    # Store refresh token and other metadata in redis
    await add_refresh_token_to_redis(redis_client, user, refresh_token, forwarded_for, user_agent, request.fingerprint)

    data = Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )

    return create_response(data=data, message="User registered successfully")


@router.post('/logout')
async def logout(request: Request):
    """Logout user and revoke JWT access and refresh tokens"""
    pass


@router.post('/refresh')
async def refresh(request: Request):
    """Refresh JWT access and refresh tokens"""
    pass
