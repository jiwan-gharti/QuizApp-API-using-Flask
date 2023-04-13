from flask import request
from ..extensions import SECRET_KEY
import jwt
from ..models.quizappmodel import User

class IsAdmin(object):
    def __init__(self,function) -> None:
        self.function=function
        pass

    def __call__(self,*args,**kwargs):
        token = None    
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return {'message' : 'Token is missing !!'}, 401
        
        
        try:
            data = jwt.decode(token,SECRET_KEY,"HS256")
            user = User.get_by_id(data['user'])
        except Exception as e:
            print(e)
            return {'message' : 'Token is invalid !!'}, 401
        
        return self.function(self,user,*args,**kwargs)


