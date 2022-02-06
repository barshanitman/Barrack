
from database import Base,engine 

from models import UserType,Users


Base.metadata.create_all(engine)