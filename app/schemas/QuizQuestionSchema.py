from marshmallow import Schema,fields, validate
from ..schemas.QuestionTypeSchema import QuestionTypeSchema
from ..schemas.QuizSchema import QuizSchema


class QuizQuestionSchema(Schema):
    id = fields.Str()
    question = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )
    choice1 = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )
    choice2 = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )
    choice3 = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )
    choice4 = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )
    correct_answer = fields.Str(
        required=True,
        validate=validate.OneOf(["1","2","3","4"])
    )
    published = fields.Boolean()
    
    quiz_id = fields.Str(required=True)
    question_type_id = fields.Str(required=True)
    # question_type = fields.Nested(
    #     QuestionTypeSchema(only=['question_type'],dump_only=['question_type'])
    # )


