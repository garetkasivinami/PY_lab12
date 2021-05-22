from DatabaseContext import db

class Album(db.Model):
    __tablename__ = 'Albums'
    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(256), nullable=False)
    Description = db.Column(db.Text(), nullable=False)
    Year = db.Column(db.Integer(), nullable=False)
    CountOfTracks = db.Column(db.Integer(), nullable=False)
    ImageUrl = db.Column(db.String(256), nullable=False)

    def __init__(self, name, description, year, countOfTracks, imageUrl):
        self.Name = name
        self.Description = description
        self.Year = year
        self.CountOfTracks = countOfTracks
        self.ImageUrl = imageUrl