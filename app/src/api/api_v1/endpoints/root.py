from fastapi import APIRouter

from src.schemas.root import HealthCheck
from src.core.config import settings

router = APIRouter()


@router.get("/")
async def health_check() -> HealthCheck:
    """Health check endpoint."""
    return HealthCheck(
        status="ok",
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

