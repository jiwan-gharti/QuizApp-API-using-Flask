
'''
user expose API class 
'''

from flask import request, jsonify
from flask_restful import Resource
from ...models.quizappmodel import Quiz,User,QuizType, Category
from ...schemas.QuizSchema import QuizSchema,UserSchema
from ...decorators.login_required_class import LoginRequired
from ...models.quizappmodel import QuizQuestion
from ...schemas.QuizQuestionSchema import QuizQuestionSchema
from ...models.quizappmodel import QuizInstanceWithGrade



from marshmallow import Schema,fields,validate

# class QuestionAnswerSchema(Schema):
#     id = fields.Str()
#     given_answer = fields.Str(required=True,validate=validate.OneOf(['1','2','3','4']))
#     question_id = fields.Str(required=True)
#     user_id = fields.Str(
#         required=True, 
#         dump_only=True
#     )
#     quiz = fields.Nested(QuizSchema(),only=['id','title'])


from marshmallow import Schema,fields

class ResultSchema(Schema):
    id = fields.Str()
    user_id = fields.Str(
        required=True, 
        dump_only=True
    )
    quiz = fields.Nested(QuizSchema(),only=['id','title'])
    is_submitted = fields.Str(dump_only=True)
    is_active = fields.Str(dump_only=True)
    score_achived = fields.Str(dump_only=True)


class AssignQuizAPI(Resource):

    @LoginRequired
    def get(self,user,quiz_id):
        quiz = Quiz.get_by_id(quiz_id)
        if not quiz:
            return {'message':"quiz doesnot exist"}, 404
        
        quiz_instance = QuizInstanceWithGrade.query.filter_by(
            user_id=user.id
        ).filter_by(
            quiz_id = quiz_id
        ).filter_by(
            is_submitted=0
        ).first()
        
        if quiz_instance:
            quiz = questions = quiz_instance.quiz
            questions = QuizQuestion.query.filter_by(quiz=quiz).filter_by(published=True).all()
            serialized_data = QuizQuestionSchema(many=True).dump(questions)
            return serialized_data, 200
        
        obj = QuizInstanceWithGrade(
            user = user,
            quiz = quiz,
            is_active = 1
        )
        obj.save()
        questions = QuizQuestion.query.filter_by(quiz_id=quiz_id).filter_by(published=True).all()
        serialized_data = QuizQuestionSchema(many=True).dump(questions)
        return serialized_data, 200
    

    @LoginRequired
    def post(self,user,quiz_id):
        """get final call
        api hit pattern:
            [
                {
                "question_id":"question_id",
                "answer":"answer_option",
                },
                {
                "question_id":"question_id",
                "answer":"answer_option",
                }
            ]
        
        Keyword arguments:
        argument -- quiz_id
        Return: score
        """
        
        json_data = request.get_json()
        quiz = Quiz.get_by_id(quiz_id)
        

        score = 0
        for data in json_data:
            question= QuizQuestion.get_by_id(data['question_id'])
            if question.correct_answer == data['answer']:
                score += 1
        else:
            try:
                quiz_instance = QuizInstanceWithGrade.query.filter_by(
                    user=user,
                    quiz=quiz
                ).first()
                if quiz_instance:
                    quiz_instance.score_achived = score
                    quiz_instance.is_submitted = 1
                    quiz_instance.is_active = 0

                    print(quiz_instance)

                    quiz_instance.save()
                    serialized_data = ResultSchema().dump(quiz_instance)
                    return serialized_data
                return {"message":"can not find quiz"}, 404
            except:
                return {"message":"something went wrong"}, 500
    
    # @LoginRequired
    # def patch(self,user,quiz_id):
    #     json_data = request.get_json()
    #     errors = QuestionAnswerSchema().validate(json_data)
    #     if errors:
    #         return {"errors":errors}, 404
        
    #     quiz = Quiz.get_by_id(quiz_id)
    #     question = QuizQuestion.get_by_id(json_data["question_id"])
        
    #     obj = QuestionAnswer.query.filter_by(
    #         user=user
    #     ).filter_by(
    #         quiz = quiz
    #     ).filter_by(
    #         question=question
    #     ).first()

    #     if not obj:
    #         obj = QuestionAnswer(
    #             user=user,
    #             quiz=quiz,
    #             question = question,
    #         )
    #         obj.save()
    #     else:
    #         obj.given_answer = json_data['given_answer']
    #         obj.save()

    #     return {"message":"successfully posted answer"}, 200
        

class GetResult(Resource):
    @LoginRequired
    def get(self,user):
        results = QuizInstanceWithGrade.query.filter_by(
            user=user
        ).filter_by(
            is_submitted=1
        ).all()
        serialized_data = ResultSchema(many=True).dump(results)
        return serialized_data, 200


