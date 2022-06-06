from flask import Blueprint, request, jsonify
from flask_restful import Resource
import logging as logger
from application.api.models.users import User
from application import db
from application.api.schema.user import UserSchema

api_bp = Blueprint("api_bp", __name__, url_prefix='/api/')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserApi(Resource):

    def get(self):
        logger.debug("Inside get method")
        schema = UserSchema(many=True)
        users = User.query.all()
        return {"response": schema.dump(users) }, 200


    def post(self):
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']

        users = User(username, email, password)
        db.session.add(users)
        db.session.commit()
        logger.debug("Inside post method")
        return user_schema.jsonify(users)
        

class UserByID(Resource):

    def get(self, userId):
        logger.debug("Inside get method of user by ID")
        user = User.query.get(userId)
        return user_schema.jsonify(user)

    def put(self, userId):
        user = User.query.get(userId)
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']

        user.username = username
        user.email = email
        user.password = password

        db.session.commit()
        return user_schema.jsonify(user)
    
    def delete(self, userId):
        logger.debug("Inside delete method")
        user = User.query.get(userId)
        db.session.delete(user)
        return {"message":"inside delete method by id User-ID = {}".format(userId)}, 200

