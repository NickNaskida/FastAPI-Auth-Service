from fastapi import APIRouter, Depends, HTTPException, Request, Response, status


router = APIRouter()


@router.post('/login')
async def login(request: Request, response: Response):
    """Login user and create JWT access and refresh tokens"""
    pass


@router.post('/register')
async def register(request: Request, response: Response):
    """Register user and create JWT access and refresh tokens"""
    pass


@router.post('/logout')
async def logout(request: Request, response: Response):
    """Logout user and revoke JWT access and refresh tokens"""
    pass


@router.post('/refresh')
async def refresh(request: Request, response: Response):
    """Refresh JWT access and refresh tokens"""
    pass
