import datetime as dt
from pydantic import BaseModel 
from typing import Optional 
import secrets
from fastapi_jwt_auth import AuthJWT

class SignUpModel(BaseModel):

    firstname: str 
    lastname: str
    age: int 
    email: str 
    streetaddress: str 
    suburb: str
    postcode: int 
    usertypeid: int 
    password: str

    class Config:
        orm_mode = True 


class Settings(BaseModel):
    authjwt_secret_key: str = '3dd23276bf2070d45288f5230020f578c3f703e1fe58dfc2dcf452c76ae99438'


class LoginModel(BaseModel):
    email: str 
    password: str 

class CreatePostModel(BaseModel):
    description: str 





   
