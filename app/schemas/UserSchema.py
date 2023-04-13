from marshmallow import Schema,fields, validate



class UserSchema(Schema):
    id = fields.Str()
    username = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )
    email = fields.Email()
    password = fields.Str(
        required=True,
        validate=validate.Length(min=5,max=100)
    )
    is_admin = fields.Bool()


       


