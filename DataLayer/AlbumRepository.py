from .Repository import Repository
from Entities.Album import Album
from DatabaseContext import db

class AlbumRepository(Repository):
    def Add(self, entity):
        db.session.add(entity)
        db.session.commit()

    def Update(self, entity):
        db.session.commit()

    def Get(self, id):
        return Album.query.get(id)

    def GetAll(self):
        return Album.query.all()

    def Where(self, filterExt):
        return list(filter(filterExt, Album.query.all()))