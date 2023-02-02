from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str
    title: str
    version: str
    openapi_url: str

    class Config:
        schema_extra = {
            "example": {
                "status": "ok",
                "title": "FastAPI Authentication Service",
                "version": "0.1.0",
                "openapi_url": "/api/v1/openapi.json"
            }
        }
