from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    '''
    Category class define category per pitch
    '''
    __tablename__ = 'categories'

    # add columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))

    # save
    def save_category(self):
        '''
        Function that saves a category
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        '''
        Function that returns all the data from the categories after being queried
        '''
        categories = Category.query.all()
        return categories

#Users
class User(UserMixin,db.Model):
    '''
    User class that will help to create new Users
    '''
    __tablename__ = 'users'

    # add column
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    password_hash=db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    # securing our passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'
