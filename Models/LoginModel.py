from .FlaskFormBase import *

class LoginModel(FlaskForm):
    login=StringField("Login:", validators=[DataRequired(), Length(4)])
    password=PasswordField("Password:", validators=[DataRequired(), Length(8)])
    submit = SubmitField("Login!")