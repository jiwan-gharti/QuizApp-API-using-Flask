""""
    User Management:
        - user management API 
        - Only Admin and self can done those operations
"""

from app.extensions import db
from flask import jsonify,request
from flask_restful import Resource
from ..models.quizappmodel import User
from ..schemas.UserSchema import UserSchema
from ..decorators.login_required_class import LoginRequired
from werkzeug.security import generate_password_hash, check_password_hash

class UserListController(Resource):
    """
        class of get, post methods 
    """
    @LoginRequired
    def get(self,user):
        """get users
        
        Keyword arguments:
        argument -- no argument
        Return: User objects
        """
        
        if user.is_admin:
            users = User.get_all_users()
            serialize_data = UserSchema(many=True).dump(users)
            return serialize_data, 200
        return {"messge":"permission denied"}, 403

    def post(self):
        """ user creation method
        body: username, email, password
        returns: User
        """
        json_data = request.get_json()
        error = UserSchema().validate(data=json_data)
        if error:
            return error, 404
        obj = User(
            username=json_data['username'],
            email = json_data['email'],
            password = generate_password_hash(json_data['password'])
        )
        try:
            obj.save()
        except:
            return {"messagee":"already exists"}
        serialized_data = UserSchema().dump(obj)
        return serialized_data, 201

class UserDetailController(Resource):
    """Detail methods operation can be done
    """
    
    @LoginRequired
    def get(self,user,user_id):
        """get detail user information
        
        Keyword arguments:
        argument -- user_id
        Return: status_code
        """
        
        if user.is_admin or user.id == user_id:
            obj = User.get_by_id(user_id)
            serialized_data = UserSchema().dump(obj)
            return serialized_data, 202
        return {"messge":"permission denied"}, 403
    
    @LoginRequired
    def patch(self,user,user_id):
        """patch method
        can update the information
        only admin can perform this action.
        
        Keyword arguments:
        argument -- user_id
        Return: updated User information
        """
        
        if user.is_admin:
            obj = User.get_by_id(user_id)
            if not obj:
                return {"message":"No user found"},404
            data = request.get_json()
            error = UserSchema().validate(data,partial=True)
            if error:
                return {"message":error}, 404
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()
            serialized_data =UserSchema().dump(obj)
            return serialized_data, 200
        return {"messge":"permission denied"}, 403
        
        

    @LoginRequired
    def put(self,user, user_id):
        if user.is_admin or user_id == user_id:
            obj = User.get_by_id(id=user_id)
            if not obj:
                return jsonify({"messgae":"No user type found"})
            data = request.get_json()
            obj.password = data.get("password",obj.password)
            obj.username = data.get("username",obj.username)
            obj.email = data.get("email",obj.email)
            obj.save()
            response ={
                'id':obj.id,
                'question_type':obj.question_type
            }
            return response, 204
        return {"messge":"permission denied"}, 403
        
    
    @LoginRequired
    def delete(self,user, user_id):
        """Delete Operation
            own or admin can perform this action
        
        Arguments: user_id
        Return : status code
        """
        if user.is_admin or user_id == user.id:
            data = User.query.filter_by(id=user_id).first()
            if not data:
                return jsonify({"messgae":"No user type found"})
            data.delete()
            return {"message":"Successfully deleted."}, 200
        return {"messge":"permission denied"}, 403
        

