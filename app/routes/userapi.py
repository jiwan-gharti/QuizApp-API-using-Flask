from app.extensions import api
from flask import Blueprint
from ..controllers.userAPI.AssignQuizAPIController import AssignQuizAPI
from ..controllers.userAPI.AssignQuizAPIController import GetResult

usermainapi = Blueprint("usermainapi",__name__)

api.add_resource(AssignQuizAPI,"/api/quiz_test/<quiz_id>")
api.add_resource(GetResult,"/api/quiz_results")



