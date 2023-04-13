
""""Question type Controller"""

from flask import request, jsonify
from flask_restful import Resource
from ..models.quizappmodel import QuestionType
from ..schemas.QuestionTypeSchema import QuestionTypeSchema
from ..decorators.login_required_class import LoginRequired

class QuestionTypeController(Resource):
    @LoginRequired
    def get(self,user):
        categories = QuestionType.get_all()
        serialized_data = QuestionTypeSchema(many=True).dump(categories)
        return {"categories":serialized_data}, 200
    
    @LoginRequired
    def post(self,user):
        if user.is_admin:
            json_data = request.get_json()
            errors = QuestionTypeSchema().validate(json_data)
            if errors:
                return {"errors":errors}, 404
            obj = QuestionType(question_type=json_data['question_type'])
            obj.save()
            question_type = QuestionTypeSchema().dump(obj)

            return question_type, 201
        return {"message":"permission denied"}, 403
    
class QuestionTypeDetailController(Resource):

    @LoginRequired
    def put(self,user, question_type_id):
        if user.is_admin:
            obj = QuestionType.query.filter_by(id=question_type_id).first()
            if not obj:
                return jsonify({"messgae":"No question type found"})
            data = request.get_json()
            obj.question_type = data.get("category",obj.question_type)
            obj.save()
            serialized_data = QuestionTypeSchema().dump(obj)
            return serialized_data, 204
        return {"message":"permission denied"}, 403
    
    @LoginRequired
    def delete(self,user, question_type_id):
        if user.is_admin:
            data = QuestionType.query.filter_by(id=question_type_id).first()
            if not data:
                return jsonify({"messgae":"No question type found"})
            data.delete()
            return jsonify({"message":"Successfully deleted."}), 200
        return {"message":"permission denied"}, 403

