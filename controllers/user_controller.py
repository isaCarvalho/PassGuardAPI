from models.user import User
import re

class UserController:

    def list(self, id):
        if (id != 0):
            return User.list(id)
        else:
            return User.list()

    def save(self, name, email, password):
        
        if (not isValid(name, email, password)):
            return "Invalid"

        user = User(name, email, password)
        user.save()

        return "Success"

    def update(self, id = 0, name = "", email = "", password = ""):

        if (not isValid(name, email, password)):
            return "Invalid"        

        user = User(name, email, password)
        user.save(id)

        return "Success"

    def delete(self, id = 0):
        if (id != 0):
            return User.delete(id)
        else:
            return "Invalid"

    def isValid(self, name, email, password):

        pattern = re.compile(r"\w+@\w+.*")

        if (name.length < 3):
            return False
        
        elif (password < 8):
            return False

        elif (pattern.match(email) == None):
            return False

        else:
            return True

        