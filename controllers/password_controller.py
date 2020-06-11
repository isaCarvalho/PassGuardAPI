from models.password import Password

class PasswordController:

    def list(self, id):
        if (id != 0):
            return Password.list(id)
        else:
            return Password.list()

    def save(self, passwordDescription, passwordContent):
        
        if (not isValid(passwordDescription, passwordContent)):
            return "Invalid"

        password = Password(passwordDescription, passwordContent)
        password.save()

        return "Success"

    def update(self, id = 0, name = "", email = "", password = ""):

        if (not isValid(passwordDescription, passwordContent)):
            return "Invalid"        

        password = Password(passwordDescription, passwordContent)
        password.save(id)

        return "Success"

    def delete(self, id = 0):
        if (id != 0):
            return Password.delete(id)
        else:
            return "Invalid"

    def isValid(self, passwordDescription, passwordContent):

        if (passwordDescription.length > 255 or passwordContent < 8):
            return False
        else:
            return True

        