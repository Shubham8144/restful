from application.api.models.users import User
from flask_marshmallow import Marshmallow
from application import localapp
from marshmallow import fields



ma = Marshmallow(localapp)

class UserSchema(ma.Schema):
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
    
    password = fields.Method(load_only=True)
