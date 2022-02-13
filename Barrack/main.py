from fastapi import FastAPI
from Routes.auth import auth_router
from Routes.posts import post_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings


app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router) 
app.include_router(post_router)

