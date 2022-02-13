from fastapi import APIRouter,status,Depends
import sys 
sys.path.append('../')
from database import Session,engine
from schemas import SignUpModel,CreatePostModel
from models import Users,Post
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash,check_password_hash
from fastapi_jwt_auth import AuthJWT
from schemas import LoginModel
from fastapi.encoders import jsonable_encoder
from datetime import date


post_router = APIRouter(prefix='/post',tags=['post'])

session = Session(bind=engine)


#Route for getting all posts by userid
@post_router.get('/posts')
async def get_all_posts(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid Token')

    current_user = Authorize.get_jwt_subject()
    posts = session.query(Post,Users.firstname,Users.lastname).join(Users,Post.userid==Users.userid,isouter=True).filter(Post.userid == current_user).all()

    return jsonable_encoder(posts)

#Route for creating posts
@post_router.post('/posts')
def create_post(post:CreatePostModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid Token')
    current_user = Authorize.get_jwt_subject()
    new_post = Post(description=post.description,userid=current_user,date=str(date.today()))
    session.add(new_post)
    session.commit()
    return jsonable_encoder({"status":"success"})


