from flask_marshmallow import Marshmallow
from marshmallow import fields

from application import localapp
from application.api.models.users import User

ma = Marshmallow(localapp)


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    password = fields.Method(load_only=True)
