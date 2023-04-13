from flask_restful import Resource
from flask import request, jsonify
from ..models.quizappmodel import Role
# from ..models.UserModel import Role
from ..schemas.RoleSchema import RoleSchema


class RoleController(Resource):
    def get(self):
        roles = Role.get_all()
        serialize_data = RoleSchema(many=True).dump(roles)
        return serialize_data, 200

    def post(self):
        json_data = request.get_json()
        error = RoleSchema().validate(data=json_data)
        if error:
            return error, 404
        obj = Role(role=json_data['role'])
        obj.save()
        serialized_data = RoleSchema().dump(obj)
        return serialized_data, 201

class CategoryDetailController(Resource):
    def get(self,role_id):
        obj = Role.get_by_id(role_id)
        serialized_data = RoleSchema().dump(obj)
        return serialized_data, 202
    
    def put(self, role_id):
        obj = Role.query.filter_by(id=role_id).first()
        if not obj:
            return jsonify({"messgae":"No role found"})
        data = request.get_json()
        obj.role = data.get("category",obj.role)
        obj.save()
        serialized_data = RoleSchema().dump(obj=obj)
        return serialized_data, 204
    
    def delete(self, role_id):
        data = Role.query.filter_by(id=role_id).first()
        if not data:
            return jsonify({"messgae":"No role type found"})
        data.delete()
        return jsonify({"message":"Successfully deleted."})



    