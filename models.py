import datetime as dt
from turtle import back
import sqlalchemy as sql 
import sqlalchemy.orm as orm 
import passlib.hash as _hash 
import database as database 



class UserType(database.Base):

    __tablename__ = 'UserType'
    UserTypeID = sql.Column(sql.Integer,index=True)
    Description = sql.Column(sql.String)
    user = orm.relationship('User',back_populates='user_type')
    donate_transaction =orm.relationship('DonateTransaction')

class User(database.Base):


    __tablename__ = 'User'

    UserID = sql.Column(sql.Integer,primary_key=True,index=True)
    Email = sql.Column(sql.String,unique=True)
    Age = sql.Column(sql.Integer,nullable=False)
    City = sql.Column(sql.String)
    Suburb = sql.Column(sql.String)
    Postcode = sql.Column(sql.Integer,nullable=False)
    UserTypeID = sql.Column(sql.Integer,sql.ForeignKey(UserType.UserTypeID))

    user_type = orm.relationship('UserType',back_populates='user')
    giver = orm.relationship('DonateTransaction',back_populates='user_giver')
    receiver = orm.relationship('DonateTransaction',back_populates='user_receiver')



class DonateType(database.Base):

    __tablename__ = 'DonationType'

    DonationTypeID = sql.Column(sql.Integer,primary_key=True,index=True)
    Description = sql.Column(sql.Text,nullable=False)
    Recurring = sql.Column(sql.Boolean,nullable=False)

    donate_transaction = orm.relationship('DonateTransaction',back_populates='donate_type')


class DonateTransaction(database.Base):

    __tablename__ = 'DonationTransaction'

    DonationTransactionID = sql.Column(sql.Integer,primary_key=True,nullable=False)
    Receiver = sql.Column(sql.Integer,sql.ForeignKey(User.UserID),nullable=False)
    Giver = sql.Column(sql.Integer,sql.ForeignKey(User.UserID),nullable=False)
    DonateTypeID = sql.Column(sql.Integer,sql.ForeignKey(DonateType.DonationTypeID))
    MonetaryValue = sql.Column(sql.Float,nullable=True)
    Date_Agreed = sql.Column(sql.Date,nullable=False)
    Date_Delivered = sql.Column(sql.Date,nullable=False)

    donate_type = orm.relationship('DonateType',back_populates='donate_transaction')
    user_giver = orm.relationship('User',back_populates='giver')
    user_receiver = orm.relationship('User',back_populates='receiver')


    

