from DatabaseContext import db
import hashlib

class User(db.Model):
     __tablename__ = 'Users'

     Id = db.Column(db.Integer(), primary_key=True)
     Login = db.Column(db.String(64), nullable=False)
     Password = db.Column(db.String(64), nullable=False)
     Salt = db.Column(db.String(64), nullable=False)
     UserName = db.Column(db.String(64), nullable=False)

     def __init__(self, login, password, salt, userName):
         self.Login = login
         self.Password = password
         self.Salt = salt
         self.UserName = userName

     def GetToken(self):
         m = hashlib.sha256()
         m.update(f'{self.Id}{self.Login}{self.Password}{self.Salt}'.encode('utf-8'))
         return m.hexdigest()