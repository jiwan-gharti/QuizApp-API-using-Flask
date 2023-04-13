# from app.extensions import ma
# from marshmallow_sqlalchemy.schema import Schema, auto_field
from marshmallow import Schema,fields, ValidationError, validates,post_load, validate



class QuestionTypeSchema(Schema):
    id = fields.Str()
    question_type = fields.Str(
        required=True, 
        validate=validate.OneOf(["Easy","Hard","Moderate"])
    )


       


