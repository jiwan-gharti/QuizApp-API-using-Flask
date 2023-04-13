
from flask import request, jsonify
from flask_restful import Resource
from ..models.quizappmodel import QuizQuestion,Quiz,QuestionType
from ..schemas.QuizQuestionSchema import QuizQuestionSchema


class QuestionController(Resource):
    def get(self):
        questions = QuizQuestion.get_all()
        serialaized_data = QuizQuestionSchema(many=True).dump(questions)
        
        return {"questions":serialaized_data}, 200

    def post(self):
        json_data = request.get_json()
        errors = QuizQuestionSchema().validate(json_data)
        if errors:
            return {"errors":errors}, 404
        
        quiz = Quiz.get_by_id(json_data['quiz_id'])
        if not quiz:
            return {"message":"Quiz doesnot exist"}, 404
        question_type = QuestionType.get_by_id(json_data['question_type_id'])
        if not question_type:
            return {'message':'Question type doesnot exists'}, 404
        
        obj = QuizQuestion(
            question = json_data['question'],
            choice1 = json_data['choice1'],
            choice2 = json_data['choice2'],
            choice3 = json_data['choice3'],
            choice4 = json_data['choice4'],
            correct_answer = json_data['correct_answer'],
            question_type = question_type,
            quiz = quiz
        )
        try:
            obj.save()
        except:
            return {"message":"already exists"}, 404
        serialized_data = QuizQuestionSchema().dump(json_data)

        return serialized_data, 201

class QuestionDetailController(Resource):
    def patch(self, question_id):
        obj = QuizQuestion.get_by_id(question_id)
        if not obj:
            return jsonify({"messgae":"No question found"})
        data = request.get_json()
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        serialized_data = QuizQuestionSchema().dump(obj)

        return serialized_data, 200
    
    def put(self, question_id):
        obj = QuizQuestion.get_by_id(question_id)
        if not obj:
            return jsonify({"messgae":"No question found"})
        data = request.get_json()
        print(data.get("question",obj.question))
        obj.question = data.get("question",obj.question)
        obj.published = data.get("published",obj.published)
        obj.answer = data.get("answer",1)
        from app import db
        db.session.add(obj)
        db.session.commit()
        response ={
            'id':obj.id,
            'question':obj.question,
            "published":obj.published,
            "user_id": obj.user_id

        }
        return response, 204

    
    def delete(self,question_id):
        data = QuizQuestion.get_by_id(question_id)
        if not data:
            return jsonify({"messgae":"No question found"})
        data.delete()
        return jsonify({"message":"Successfully deleted."})






