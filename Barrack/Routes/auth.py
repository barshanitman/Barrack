from fastapi import APIRouter,status,Depends
import sys 
sys.path.append('../')
from database import Session,engine
from schemas import SignUpModel
from models import Users
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi_jwt_auth import AuthJWT
from schemas import LoginModel
from fastapi.encoders import jsonable_encoder


auth_router = APIRouter(prefix='/auth',tags=['auth'])

session = Session(bind=engine)

#Route for adding new user
@auth_router.post('/signup')
async def signup(user:SignUpModel):
    db_email = session.query(Users).filter(Users.email==user.email).first() 
    if db_email is not None:
        return HTTPExceptions(status_code=status.HTTP_400_BAD_REQUEST,details='User with this email already exists')
    new_user = Users(firstname=user.firstname,lastname=user.lastname,
            age=user.age,email=user.email,streetaddress=user.streetaddress,
            suburb=user.suburb,usertypeid=user.usertypeid,
            postcode=user.postcode,password=generate_password_hash(user.password))

    session.add(new_user)
    session.commit()
    return new_user


@auth_router.post('/login')
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):
    db_email = session.query(Users).filter(Users.email == user.email).first()
    if db_email and check_password_hash(db_email.password,user.password):
        access_token = Authorize.create_access_token(subject=db_email.userid)
        refresh_token = Authorize.create_refresh_token(subject=db_email.userid)
        return jsonable_encoder({'access_token':access_token,'refresh_token':refresh_token})
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Invalid email or password')


@auth_router.post('/refresh')
async def refresh_token(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_refresh_token_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Please provide a valid refresh token')

    current_user = Authorize.get_jwt_subject()
    access_token = Authorize.create_access_token(subject=current_user)

    return jsonable_encoder({'access_token':access_token})
