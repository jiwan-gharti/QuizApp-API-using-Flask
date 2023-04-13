from marshmallow import Schema,fields, validate
# from ..schemas.QuizSchema import QuizSchema


class QuizSchema1(Schema):
    id = fields.Str()
    title = fields.Str(
        required=True,
        validate=validate.Length(min=4,max=255)
    )
    active = fields.Boolean()
    done = fields.Bool()
    quiz_type_id = fields.Str(required=True)
    # questions = fields.Nested(QuizQuestionSchema, many=True)
    


class CategorySchema(Schema):
    id = fields.Str()
    category = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )
    quizes = fields.Nested(
        QuizSchema1, many=True
    )

       


