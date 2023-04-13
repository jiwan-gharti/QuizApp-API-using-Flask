
from flask import request, jsonify
from flask_restful import Resource
from ..models.quizappmodel import Quiz,User,QuizType, Category
from ..schemas.QuizSchema import QuizSchema,UserSchema
from ..decorators.login_required_class import LoginRequired


class QuizListController(Resource):
    @LoginRequired
    def get(self,user):
        quizes = Quiz.get_all()
        serialized_data = QuizSchema(many=True).dump(quizes)
        return serialized_data, 200

    @LoginRequired
    def post(self,user):
        json_data = request.get_json()
        errors = QuizSchema().validate(json_data)
        if errors:
            return {"errors":errors}, 404
        
        user = User.get_by_id(json_data['user_id'])
        if not user:
            return {'message':"user doesnot exist"}, 404
        
        quiz_type = QuizType.get_by_id(json_data['quiz_type_id'])
        if not quiz_type:
            return {"message":"Quiz type doesnot exist"}
        
        obj = Quiz(
            title=json_data['title'],
            user = user,
            quiz_type=quiz_type
        )
        categories = json_data.get('categories_id',None)

        try:
            if categories is not None:
                for category in categories:
                    category_obj = Category.get_by_id(category)
                    if category_obj:
                        obj.categories.append(category_obj)   
        except:
            return {"messag":"not a valid categories"},404  
        try:
            obj.save()
        except Exception as e:
            return {"messagae":"already exists."},404
        serialized_data = QuizSchema().dump(obj)

        return serialized_data, 201
    
class QuizDetailController(Resource):
    @LoginRequired
    def get(self,user,quiz_id):
        quizes = Quiz.quiz_type_id(quiz_id)
        serialized_data = QuizSchema(many=True).dump(quizes)
        return {"quizes":serialized_data}, 200
    
    @LoginRequired
    def patch(self,user,quiz_id):
        if user.is_admin:
            json_data = request.get_json()
            errors = QuizSchema().validate(json_data,partial=True)
            if errors:
                return {"errors":errors}, 404
            quiz = Quiz.get_by_id(quiz_id)
            if not quiz:
                return {"message":"Not found"}, 404
            for key,value in json_data.items():
                setattr(quiz,key,value)
            categories = json_data.get('categories_id',None)
            
            try:
                if categories is not None:
                    for category in categories:
                        category_obj = Category.get_by_id(category)
                        if category_obj:
                            quiz.categories.append(category_obj)   
            except:
                return {"messag":"not a valid categories"},404  
            try:
                quiz.save()
            except:
                return {"message":"Invalid Datatype"}
            serialized_data = QuizSchema().dump(quiz)
            return serialized_data, 200
        return {"message":"permission denied"}, 403
    
    @LoginRequired
    def put(self, user, quiz_id):
        quiz = Quiz.get_by_id(quiz_id)
        if not quiz:
            return jsonify({"messgae":"No quiz found"})
        json_data = request.get_json()
        errors = QuizSchema().validate(json_data)
        if errors:
            return {"errors":errors}, 404
        for key,value in json_data.items():
            setattr(quiz,key,value)
            
        categories = json_data.get('categories_id',None)
        try:
            if categories is not None:
                for category in categories:
                    category_obj = Category.get_by_id(category)
                    if category_obj:
                        quiz.categories.append(category_obj)   
        except:
            return {"messag":"not a valid categories"},404  
        
        quiz.save()
        serialized_data = QuizSchema().dump(quiz)
        return serialized_data, 200
    
    @LoginRequired
    def delete(self,user, quiz_id):
        """Delete Operation
        Only responsible for admin
        
        Keyword arguments:
        argument -- quiz_id
        Return: status_code
        """
        if user.is_admin:
            data = Quiz.get_by_id(quiz_id)
            if not data:
                return jsonify({"messgae":"No quiz found"})
            data.delete()
            return jsonify({"message":"Successfully deleted."}), 200
        return {"message":"permission denied"}, 403



    