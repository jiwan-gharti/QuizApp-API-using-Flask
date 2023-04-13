from marshmallow import Schema,fields, validate



class RoleSchema(Schema):
    id = fields.Str()
    role = fields.Str(
        required=True, 
        validate=validate.Length(min=3,max=20)
    )

       


