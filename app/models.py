from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import db
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'User {self.username}'

class EplStandings:
    '''
    articles class to define the article Objects
    '''
    def __init__(self,position,matches,team_name,wins,draws,losses,goaldifference,points):
        # self.id=id
        self.position=position
        self.matches=matches
        self.team_name=team_name
        self.wins=wins
        self.draws=draws
        self.losses=losses
        self.goaldifference=goaldifference
        self.points=points
