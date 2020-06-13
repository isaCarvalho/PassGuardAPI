from models.register import Register
import hashlib

class RegisterController:

    def list(self, id):
        if (id != 0):
            return Register.list(id)
        else:
            return Register.list()

    def encrypt(self, passwordDescription, passwordContent):
        return hashlib.md5(passwordDescription), hashlib.md5(passwordContent)

    def save(self, passwordDescription, passwordContent, id_user):
        
        passwordDescription, passwordContent = self.encrypt(passwordDescription, passwordContent)

        password = Register(passwordDescription, passwordContent, id_user)
        return password.save()

    def update(self, passwordDescription, passwordContent, id_user, id = 0):       

        passwordDescription, passwordContent = self.encrypt(passwordDescription, passwordContent)

        password = Register(passwordDescription, passwordContent, id_user)
        return password.save(id)

        return "success"

    def delete(self, id = 0):
        if (id != 0):
            return Register.delete(id)
        else:
            return "invalid"

    def getRegisterByUser(self, id_user):
        if (id_user == None or id_user == 0):
            return "invalid"
        else:
            return Register.getRegisterByUser(id_user)