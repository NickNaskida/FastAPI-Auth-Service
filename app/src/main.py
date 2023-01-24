import uvicorn
from fastapi import FastAPI
from starlette_context import middleware, plugins
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware


from src.api.api_v1.api import api_router
from src.core.config import settings
from src.db.url import get_sqlalchemy_url


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    SQLAlchemyMiddleware,
    db_url=get_sqlalchemy_url(),
    engine_args={
        "echo": False,
        "pool_pre_ping": True,
        "pool_size": settings.SQLALCHEMY_POOL_SIZE,
        "max_overflow": settings.SQLALCHEMY_MAX_OVERFLOW,
    }
)

app.add_middleware(
    middleware.ContextMiddleware,
    plugins=(
        plugins.ForwardedForPlugin(),
        plugins.UserAgentPlugin()
    )
)


app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(app, port=8000, proxy_headers=True, log_level="debug")
