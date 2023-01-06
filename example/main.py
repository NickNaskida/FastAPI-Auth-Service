from fastapi import FastAPI

from fastapi_secure_jwt.router.auth import auth_router

app = FastAPI()
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
