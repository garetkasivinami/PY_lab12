from flask_sqlalchemy import SQLAlchemy
from ApplicationContext import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)