from marshmallow import Schema
from marshmallow import Schema,fields, validates,post_load, validate

from ..schemas.CategorySchema import CategorySchema
from ..schemas.QuizTypeSchema import QuizTypeSchema
from ..schemas.UserSchema import UserSchema


class QuizSchema(Schema):
    id = fields.Str()
    title = fields.Str(
        required=True,
        validate=validate.Length(min=4,max=255)
    )
    active = fields.Boolean()
    done = fields.Bool()

    categories_id = fields.List(fields.Str(),required=True,load_only=True)
    categories = fields.Nested(CategorySchema(only=["id","category"]), many=True,dump_only=True)

    quiz_type_id = fields.Str(required=True,load_only=True)
    quiz_type = fields.Nested(QuizTypeSchema,dump_only=True,only=["id","quiz_type"])

    user_id = fields.Str(required=True,load_only=True)
    # user = fields.Nested(UserSchema,dump_only=True,only=['id','email'])
    
    # questions = fields.Nested(QuizQuestionSchema,many=True,dump_only=True)
    

    
