from models.register import Register

class RegisterController:

    def list(self, id):
        if (id != 0):
            return Register.list(id)
        else:
            return Register.list()

    def save(self, passwordDescription, passwordContent, id_user):
        
        password = Register(passwordDescription, passwordContent, id_user)
        return password.save()

    def update(self, passwordDescription, passwordContent, id_user, id = 0):       

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