from flask_sqlalchemy import SQLAlchemy
# from marshmallow
from flask_migrate import Migrate
from flask_restful import Api


db = SQLAlchemy()
# ma = marshmallow()
migrate = Migrate()
api = Api()

SECRET_KEY = 'secret'