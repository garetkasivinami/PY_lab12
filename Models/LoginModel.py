from .FlaskFormBase import *

class LoginModel(FlaskForm):
    login=StringField("Login:", validators=[DataRequired(), Length(min=4, max=64)])
    password=PasswordField("Password:", validators=[DataRequired(), Length(8)])
    submit = SubmitField("Login!")