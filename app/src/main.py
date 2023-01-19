from fastapi import FastAPI

from src.api.api_v1.api import api_router
from src.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.get("/", tags=["status"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "title": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "openapi_url": f"{settings.API_V1_STR}/openapi.json"
    }


app.include_router(api_router, prefix=settings.API_V1_STR)
