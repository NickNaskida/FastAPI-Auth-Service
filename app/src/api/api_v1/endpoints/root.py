from fastapi import APIRouter

from src.core.config import settings

router = APIRouter()


@router.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "title": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "openapi_url": f"{settings.API_V1_STR}/openapi.json"
    }
