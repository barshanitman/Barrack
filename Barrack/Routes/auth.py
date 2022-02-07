from fastapi import APIRouter,status
import sys 
sys.path.append('../')
from database import Session,engine
from schemas import SignUpModel
from models import Users
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash


auth_router = APIRouter(prefix='/auth',tags=['auth'])

session = Session(bind=engine)

#Route for adding new user
@auth_router.post('/signup')
async def signup(user:SignUpModel):
    db_email = session.query(Users).filter(Users.email==user.email).first() 
    if db_email is not None:
        return HTTPExceptions(status_code=status.HTTP_400_BAD_REQUEST,details='User with this email already exists')
    new_user = Users(userid=user.userid,firstname=user.firstname,lastname=user.lastname,
            age=user.age,email=user.email,streetaddress=user.streetaddress,
            suburb=user.suburb,usertypeid=user.usertypeid,
            postcode=user.postcode,password=generate_password_hash(user.password))

    session.add(new_user)
    session.commit()
    return new_user



