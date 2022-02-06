import sqlalchemy as sql 
import sqlalchemy.orm as orm 
import passlib.hash as _hash 
import sqlalchemy as sql 
import sqlalchemy.ext.declarative as declarative 
import sqlalchemy.orm as orm 
import database 


class UserType(database.Base):

    __tablename__ = 'usertype'

    usertypeid = sql.Column(sql.Integer,primary_key=True,index=True)
    description = sql.Column(sql.String,nullable=False)

    user = orm.relationship('user',backref='usertype')
    

class Users(database.Base):

    __tablename__ = 'users'

    userid = sql.Column(sql.Integer,primary_key=True,index=True)
    firstname = sql.Column(sql.String,nullable=False)
    lastname = sql.Column(sql.String,nullable=False)
    age = sql.Column(sql.Integer,nullable=False)
    streetaddress = sql.Column(sql.String,nullable=False)
    postcode = sql.Column(sql.Integer,nullable=False)
    usertypeid = sql.Column(sql.Integer,sql.ForeignKey('usertype.usertypeid'))


class DonationType:

    __tablename__ = 'donationtype'

    donationtypeid = sql.Column(sql.Integer,primary_key=True,index=True)
    description = sql.Column(sql.String,nullable=False)
    donationtransaction = orm.relationship('donationtransaction',backref='donationtype')

    
class Transaction(database.Base):
    __tablename__ = 'transaction'

    transactionid = sql.Column(sql.Integer,primary_key=True,index=True)
    dateagreed = sql.Column(sql.Date,nullable=False)
    giverid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))
    receiverid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))

    completed_transaction = orm.relationship('')


class CompletedTransaction(database.Base):

    __tablename__ = 'completedtransaction'

    completedtransactionid = sql.Column(sql.Integer,primary_key=True,index=True)
    transactionid = sql.Column(sql.Integer,sql.ForeignKey('transaction.transactionid'))
    datecompleted = sql.Column(sql.Date,nullable=False)






    










   


    
