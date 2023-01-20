from fastapi import APIRouter

from src.api.api_v1.endpoints import root, auth

api_router = APIRouter()
api_router.include_router(root.router, tags=["status"])
api_router.include_router(auth.router, tags=["auth"])

