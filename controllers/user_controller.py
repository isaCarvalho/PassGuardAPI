from models.user import User
import re
import hashlib

class UserController:

    def list(self, id):
        if (id != 0):
            return User.list(id)
        else:
            return User.list()

    def encrypt(self, email, password):
        return hashlib.md5(email), hashlib.md5(password)

    def save(self, name, email, password):

        name = hashlib.md5(name)
        email, password = self.encrypt(email, password)

        user = User(name, email, password)
        return user.save()                             

    def update(self, id = 0, name = "", email = "", password = ""):    

        name = hashlib.md5(name)
        email, password = self.encrypt(email, password)

        user = User(name, email, password)
        return user.save(id)

    def delete(self, id = 0):
        if (id != 0):
            return User.delete(id)
        else:
            return "fail"

    def authenticate(self, email, password, encrypt):
        if (email == None or password == None):
            return "invalid"

        if (encrypt == None or encrypt == "false"):
            email, password = self.encrypt(email, password)

        return User.login(email, password)