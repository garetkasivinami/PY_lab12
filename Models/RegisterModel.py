from .FlaskFormBase import *
from .LoginModel import LoginModel

class RegisterModel(LoginModel):
    username=StringField("Username:", validators=[DataRequired(), Length(min=4, max=64)])
    submit = SubmitField("Register!")
