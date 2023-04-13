from app.extensions import api
from flask import Blueprint
from ..controllers.AuthController import AuthController
from ..controllers.UserController import UserListController, UserDetailController
from ..controllers.QuizController import QuizListController, QuizDetailController
from ..controllers.CategoryController import CategoryController, CategoryDetailController
from ..controllers.QuizTypeController import QuizTypeController, QuizTypeDetailController
from ..controllers.QuizQuestionController import QuestionController,QuestionDetailController
from ..controllers.QuestionTypeController import QuestionTypeController, QuestionTypeDetailController

main = Blueprint("main",__name__,url_prefix="/api")

api.add_resource(AuthController, '/api/auth')

api.add_resource(UserListController, '/api/user')
api.add_resource(UserDetailController, "/api/user/<user_id>")

api.add_resource(QuizListController, '/api/quiz')
api.add_resource(QuizDetailController, "/api/quiz/<quiz_id>")

api.add_resource(QuestionController, '/api/question')
api.add_resource(QuestionDetailController, "/api/question/<question_id>")



api.add_resource(QuestionTypeController, '/api/question_type')
api.add_resource(QuestionTypeDetailController, "/api/question_type/<question_type_id>")

api.add_resource(CategoryController, '/api/category')
api.add_resource(CategoryDetailController,"api//category/<category_id>")


api.add_resource(QuizTypeController, '/api/quiz_type')
api.add_resource(QuizTypeDetailController, "/api/quiz_  type/<quiz_type_id>")



