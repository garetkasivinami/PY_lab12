from .FlaskFormBase import *
from .LoginModel import LoginModel

class RegisterModel(LoginModel):
    username=StringField("Username:", validators=[DataRequired(), Length(4)])
    submit = SubmitField("Register!")
