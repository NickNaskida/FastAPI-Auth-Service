from fastapi import FastAPI

from fastapi_secure_jwt.router.auth import auth_router
from fastapi_secure_jwt.jwt import generate_jwt_token, decode_jwt_token

app = FastAPI()
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"],
)

SECRET_KEY = "NOT_A_SECRET_KEY"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/token")
async def get_token():
    return generate_jwt_token(
        "NickNaskida",
        "access",
        SECRET_KEY,
        lifetime=60 * 15,
        claims={
            "name": "Nick Naskidashvili",
            "email": "nick@gmail.com",
            "age": 25,
            "role": "admin"
        }
    )


@app.get("/decode-token")
async def decode_token(token: str):
    return decode_jwt_token(
        token,
        SECRET_KEY
    )
