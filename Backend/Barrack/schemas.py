import datetime as dt
import pydantic

from models import DonateTransaction 


class UserTypeBase(pydantic.BaseModel):
    UserTypeID: int 
    Description: str 


class UserBase(pydantic.BaseModel):
    UserID: int 
    Email: str
    Age: int 
    City: str 
    Suburb: str
    Postcode: int 
    UserTypeID: int 


class DonateTypeBase(pydantic.BaseModel):
    DontationTypeID: int 
    Description: str 
    Recurring: bool

class DonateTransactionBase(pydantic.BaseModel):
    DonateTransactionID: int 
    Receiver: int 
    Giver: int 
    DonateTypeID: int 
    PledgeID: int 
    MonetaryValue: float 
    Delivered: bool
    DateDelivered: dt.date

