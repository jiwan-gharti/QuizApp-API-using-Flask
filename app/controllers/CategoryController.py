"""
    category controller:
        - Its responsibility is to provide category CRUD operation
        - Only admin can perform those actions 
"""

from app.extensions import db
from flask import request, jsonify
from flask_restful import Resource
from ..models.quizappmodel import Category
from ..schemas.CategorySchema import CategorySchema
from ..decorators.login_required_class import LoginRequired


class CategoryController(Resource):
    """
        class: CategoryController
    """

    @LoginRequired
    def get(self,user):
        """Get Operation
        authenticated user can perform this action
        Returns: categories objects
        """
        
        categories = Category.get_all()
        serialize_data = CategorySchema(many=True).dump(categories)
        return serialize_data, 200


    @LoginRequired
    def post(self,user):
        '''Post operation
        Only admin can perform this action
        Body: category: str
        Returns: Category serialized object
        '''
        if user.is_admin:
            json_data = request.get_json()
            error = CategorySchema().validate(data=json_data)
            if error:
                return error, 404
            try:
                obj = Category(category=json_data['category'])
                obj.save()
            except Exception as e:
                return {'message':"already exists"}, 404
            serialized_data = CategorySchema().dump(obj)
            return serialized_data, 201
        else:
            return {'messgae':"no permission"}, 403

class CategoryDetailController(Resource):
    """Category Detail API Controller"""
    

    @LoginRequired
    def get(self,user,category_id):
        """get category detail
        
        Keyword arguments:
        argument -- category_id: int
        Return: category object
        """
        
        obj = Category.get_by_id(category_id)
        serialized_data = CategorySchema().dump(obj)
        return serialized_data, 202
    
    @LoginRequired
    def patch(self,user,category_id):
        """Patch Operation 
        
        Keyword arguments:
        argument -- category_id: int
        Return: updated_category_serialized Object
        """
        
        if user.is_admin:
            obj = Category.query.filter_by(id=category_id).first()
            if not obj:
                return jsonify({"messgae":"No question type found"})
            data = request.get_json()
            obj.question_type = data.get("category",obj.category)
            db.session.add(obj)
            db.session.commit()
            response ={
                'id':obj.id,
                'question_type':obj.question_type
            }
            return response, 204
        return {"message":"no permission"}, 401
        
    @LoginRequired
    def put(self, category_id):
        obj = Category.query.filter_by(id=category_id).first()
        if not obj:
            return jsonify({"messgae":"No question type found"})
        data = request.get_json()
        obj.question_type = data.get("category",obj.category)
        db.session.add(obj)
        db.session.commit()
        response ={
            'id':obj.id,
            'question_type':obj.question_type
        }
        return response, 204
    
    @LoginRequired
    def delete(self,user, category_id):
        if user.is_admin:
            data = Category.query.filter_by(id=category_id).first()
            if not data:
                return jsonify({"messgae":"No question type found"})
            data.delete()
            return jsonify({"message":"Successfully deleted."})
        return {"messge": "permission denied"}, 40



    