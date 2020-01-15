from flask_restful import Resource

from db.model import UserModel


class UserView(Resource):

    def __init__(self):
        self.model = UserModel

    def get(self, id=None):
        if id:
            return self.model.query.filter(id=id).all()
        return self.model.query.all()

    def post(self, id):
        ...

    def put(self, id):
        ...

    def delete(self, id):
        ...


