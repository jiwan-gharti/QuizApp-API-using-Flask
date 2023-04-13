

from flask import Flask
from .routes.api import main
from .routes.userapi import usermainapi
from .extensions import (
    # ma,
    api,
    db,
    migrate,
    SECRET_KEY
)

# from flask_swagger_ui import get_swaggerui_blueprint

# SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
# API_URL = '/static/swagger.json' 
# # API_URL = 'http://petstore.swagger.io/v2/swagger.json' 



# # Call factory function to create our blueprint
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     config={  # Swagger UI config overrides
#         'app_name': "Test application"
#     },
#     # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#     #    'clientId': "your-client-id",
#     #    'clientSecret': "your-client-secret-if-required",
#     #    'realm': "your-realms",
#     #    'appName': "your-app-name",
#     #    'scopeSeparator': " ",
#     #    'additionalQueryStringParams': {'test': "hello"}
#     # }
# )



def create_app():
    # Init
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../sqlite3.db"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config['SECRET_KEY'] = SECRET_KEY
    app.config.from_object("config")


    # api
    db.init_app(app=app)
    api.init_app(app=app)
    # ma.init_app(app=app)
    migrate.init_app(app=app,db=db)
    # app.register_blueprint(swaggerui_blueprint)


    with app.app_context():
        db.create_all()


    app.register_blueprint(main)
    app.register_blueprint(usermainapi)


    return app




