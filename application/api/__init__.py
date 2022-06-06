from flask_restful import Api
from .views.main import UserApi, UserByID, api_bp

restserver = Api(api_bp)

restserver.add_resource(UserApi, "/v1.0/task")
restserver.add_resource(UserByID, "/v1.0/task/<string:userId>")
