
"""Quiz Type Controller
Eg. Science or Math or Gk or Programming
"""

from flask import request, jsonify
from flask_restful import Resource
from ..models.quizappmodel import QuizType
from ..schemas.QuizTypeSchema import QuizTypeSchema
from ..decorators.login_required_class import LoginRequired

class QuizTypeController(Resource):
    """List and Post methods Controller"""

    @LoginRequired
    def get(self,user):
        quiz_types = QuizType.get_all()
        serialized_data = QuizTypeSchema(many=True).dump(quiz_types)
        
        return {"quiz_types":serialized_data}, 200
    
    @LoginRequired
    def post(self,user):
        if user.is_admin:
            json_data = request.get_json()
            errors = QuizTypeSchema().validate(json_data)
            if errors:
                return {"message":errors},404
            obj = QuizType(quiz_type=json_data['quiz_type'])
            obj.save()
            serialized_data = QuizTypeSchema().dump(obj)
            return serialized_data, 201
        return {"messagae":"permission denied"}, 403

class QuizTypeDetailController(Resource):
    """Detail Methods of Quiz Type"""

    def get(self,quiz_type_id):
        obj = QuizType.get_by_id(quiz_type_id)
        serialized_data = QuizTypeSchema().dump(obj)
        return serialized_data, 201
    
    @LoginRequired
    def put(self,user, quiz_type_id):
        if user.is_admin:
            obj = QuizType.query.filter_by(id=quiz_type_id).first()
            if not obj:
                return jsonify({"messgae":"No quiz found"})
            data = request.get_json()
            obj.quiz_type = data.get("quiz_type",obj.quiz_type)
            obj.save()
            serialized_data = QuizTypeSchema().dump(obj)
            return serialized_data, 200
        return {"message":"permission denied"}, 403
        
    
    @LoginRequired
    def delete(self, user,quiz_type_id):
        """Delete Operation
        Body: quiz_id
        """
        
        if user.is_admin:
            data = QuizType.query.filter_by(id=quiz_type_id).first()
            if not data:
                return {"messgae":"No quiz found"}, 404
            data.delete()
            return {"message":"Successfully deleted."}, 200
        return {'message': "permission denied"}, 403 
    

