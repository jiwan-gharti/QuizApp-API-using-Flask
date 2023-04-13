"""
    QuizApp Authentication Token generator
"""

import jwt
import datetime
from flask import request,jsonify
from flask_restful import Resource
from ..extensions import SECRET_KEY
from ..models.quizappmodel import User
from werkzeug.security import check_password_hash



class AuthController(Resource):
    """class for generating token
    """
    
    def post(self):
        """post method 
        
        Keyword arguments:
        argument -- email, password
        Return: sh256_token
        """
        
        data = request.get_json()
        user = User.get_user_for_auth(
            email=data['email']
        )
        print(user.id)
        if not user and check_password_hash(user.password, SECRET_KEY):
            return {"message":"Email or password incorrect"}, 404
        
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=10)
        epoch_time = int(exp.timestamp())
        payload = {
            "user": user.id,
            "exp": epoch_time
        }
        token = jwt.encode(payload=payload,key=SECRET_KEY,algorithm="HS256")
        return {"token":token}, 200

