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

    user = orm.relationship('Users',backref='usertype')


class Users(database.Base):

    __tablename__ = 'users'

    userid = sql.Column(sql.Integer,primary_key=True,index=True)
    firstname = sql.Column(sql.String,nullable=False)
    lastname = sql.Column(sql.String,nullable=False)
    age = sql.Column(sql.Integer,nullable=False)
    email = sql.Column(sql.String,nullable=False,unique=True)
    streetaddress = sql.Column(sql.String,nullable=False)
    postcode = sql.Column(sql.Integer,nullable=False)
    usertypeid = sql.Column(sql.Integer,sql.ForeignKey('usertype.usertypeid'))

    password = orm.relationship('Password',backref='users')
    comment = orm.relationship('Comment',backref='users')
    heartuser = orm.relationship('PostHearts',backref='users')




class Password(database.Base):

    __tablename__ ='password'
    passwordid = sql.Column(sql.Integer,primary_key=True,index=True)
    password = sql.Column(sql.String,nullable=False) 
    userid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))






class DonationType(database.Base):

    __tablename__ = 'donationtype'

    donationtypeid = sql.Column(sql.Integer,primary_key=True,index=True)
    description = sql.Column(sql.String,nullable=False)
    donationtransaction = orm.relationship('Transaction',backref='donationtype')



class Transaction(database.Base):

    __tablename__ = 'transaction'

    transactionid = sql.Column(sql.Integer,primary_key=True,index=True)
    donationtypeid = sql.Column(sql.Integer,sql.ForeignKey('donationtype.donationtypeid'))
    dateagreed = sql.Column(sql.Date,nullable=False)
    giverid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))
    receiverid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))
    completed_transaction = orm.relationship('CompletedTransaction',backref='transaction')


class CompletedTransaction(database.Base):

    __tablename__ = 'completedtransaction'

    completedtransactionid = sql.Column(sql.Integer,primary_key=True,index=True)
    transactionid = sql.Column(sql.Integer,sql.ForeignKey('transaction.transactionid'))
    datecompleted = sql.Column(sql.Date,nullable=False)


class Post(database.Base):

    __tablename__ = 'post'

    postid = sql.Column(sql.Integer,primary_key=True,index=True) 
    description = sql.Column(sql.Text,nullable=False)
    userid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))
    date = sql.Column(sql.Date,nullable=False)

    comment = orm.relationship('Comment',backref='post')


class Comment(database.Base):

    __tablename__ = 'comment'

    commentid = sql.Column(sql.Integer,primary_key=True,index=True)
    description = sql.Column(sql.Text,nullable=False)
    postid = sql.Column(sql.Integer,sql.ForeignKey('post.postid'))
    usercommentid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))
    date = sql.Column(sql.Date,nullable=False) 
    commenthearts = orm.relationship('CommentHearts',backref='comment')


class PostHearts(database.Base):

    __tablename__ = 'posthearts'

    postheartsid = sql.Column(sql.Integer,primary_key=True,index=True) 
    postid = sql.Column(sql.Integer,sql.ForeignKey('post.postid'))
    heartuserid = sql.Column(sql.Integer,sql.ForeignKey('users.userid'))


class CommentHearts(database.Base):

    __tablename__ = 'commenthearts'

    commentheartsid = sql.Column(sql.Integer,primary_key=True,index=True)
    commentid = sql.Column(sql.Integer,sql.ForeignKey('comment.commentid'))

