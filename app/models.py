from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    passwd = db.Column(db.String(64))
    def __repr__(self):
        return '<User %r>' % self.username

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    taskname = db.Column(db.String)
