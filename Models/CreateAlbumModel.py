from .FlaskFormBase import *

class CreateAlbumModel(FlaskForm):
    name=StringField("Name:", validators=[DataRequired(), Length(max=256)])
    description=TextField("Description:", validators=[], widget=TextArea())
    year=IntegerField("Year:", validators=[DataRequired(), NumberRange(min=1900,max=2100)])
    countOfTracks=IntegerField("Count of tracks:", validators=[DataRequired(), NumberRange(min=0,max=99999)])
    imageUrl=StringField("Image URL:", validators=[])
    submit = SubmitField("Create!")