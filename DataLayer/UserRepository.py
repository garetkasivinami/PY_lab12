from .Repository import Repository
from Entities.User import User
from DatabaseContext import db

class UserRepository(Repository):

    def Update(self, entity):
        db.session.commit()

    def Get(self,id):
        return User.query.get(id)

    def GetAll(self):
        return User.query.all()

    def Remove(self, id):
        db.session.delete(id)
        db.session.commit()