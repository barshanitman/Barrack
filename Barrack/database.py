import sqlalchemy as sql 
import sqlalchemy.ext.declarative as declarative 
import sqlalchemy.orm as orm 


DATABASE_URL = 'postgresql://rjdzcxyl:XS6Lw8hFz2TcSoeFuUBirRpH3IG5ulSZ@rosie.db.elephantsql.com/rjdzcxyl'
engine = sql.create_engine(DATABASE_URL)


Base = declarative.declarative_base()


Session = orm.sessionmaker()
