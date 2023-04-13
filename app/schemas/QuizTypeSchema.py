# from app.extensions import ma
# from marshmallow_sqlalchemy.schema import Schema, auto_field
from marshmallow import Schema,fields, ValidationError, validates,post_load, validate



class QuizTypeSchema(Schema):
    id = fields.Str()
    quiz_type = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )