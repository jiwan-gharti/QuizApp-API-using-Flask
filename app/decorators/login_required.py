
from functools import wraps
from flask import request,jsonify
import jwt
from ..extensions import SECRET_KEY
from ..models.quizappmodel import User

def login_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return {'message' : 'Token is missing !!'}, 401
        
        print(token)
        
        try:
            data = jwt.decode(token,SECRET_KEY,"HS256")
            print("data",data)
            user = User.get_by_id(data['user'])
            return f(user,*args,**kwargs)
        except Exception as e:
            print(e)
            return {'message' : 'Token is invalid !!'}, 401
        
    
    return decorator