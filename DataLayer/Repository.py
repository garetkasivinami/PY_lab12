from DatabaseContext import db

class Repository:
    def Add(self, entity):
        db.session.add(entity)
        db.session.commit()

    def Remove(self, entity):
        db.session.delete(entity)
        db.session.commit()

    def Update(self, entity):
        db.session.commit()

    def GetAll(self):
        pass

    def Get(id):
        pass

    def Where(self, filterExt):
        return list(filter(filterExt, self.GetAll()))