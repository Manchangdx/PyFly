from bson.objectid import ObjectId, InvalidId
from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        try:
            return ObjectId(value)
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()

    def to_url(self, value):
        return str(value)
