from fastapi import HTTPException, status
from starlette_context import context


def get_auth_headers() -> tuple:
    """Get headers from context"""

    # forwarded_for = context.data.get('X-Forwarded-For')  # TODO: Figure out why this return None
    forwarded_for = "00.00.00.00"
    user_agent = context.data.get('User-Agent')

    if not forwarded_for:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Missing X-Forwarded-For header')
    elif not user_agent:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Missing User-Agent header')

    return forwarded_for, user_agent
