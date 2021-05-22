from .CreateAlbumModel import CreateAlbumModel
from .FlaskFormBase import *

class EditAlbumModel(CreateAlbumModel):
    id = HiddenField('id')
    submit = SubmitField("Update!")