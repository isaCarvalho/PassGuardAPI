from models.user import User
import re

class UserController:

    def list(self, id):
        if (id != 0):
            return User.list(id)
        else:
            return User.list()

    def save(self, name, email, password):

        user = User(name, email, password)
        return user.save()

    def update(self, id = 0, name = "", email = "", password = ""):    

        user = User(name, email, password)
        return user.save(id)

    def delete(self, id = 0):
        if (id != 0):
            return User.delete(id)
        else:
            return "fail"