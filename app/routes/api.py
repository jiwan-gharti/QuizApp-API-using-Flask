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

api.add_resource(AuthController, '/auth')

api.add_resource(QuizListController, '/quiz')
api.add_resource(QuizDetailController, "/quiz/<quiz_id>")

api.add_resource(UserListController, '/user')
api.add_resource(UserDetailController, "/user/<user_id>")

api.add_resource(QuestionController, '/question')
api.add_resource(QuestionDetailController, "/question/<question_id>")



api.add_resource(QuestionTypeController, '/question_type')
api.add_resource(QuestionTypeDetailController, "/question_type/<question_type_id>")

api.add_resource(CategoryController, '/category')
api.add_resource(CategoryDetailController,"/category/<category_id>")


api.add_resource(QuizTypeController, '/quiz_type')
api.add_resource(QuizTypeDetailController, "/quiz_  type/<quiz_type_id>")



