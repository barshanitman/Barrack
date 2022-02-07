import datetime as dt
from pydantic import BaseModel 
from typing import Optional 

class SignUpModel(BaseModel):

    userid: Optional[int]
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




   
