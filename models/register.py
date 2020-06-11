from dao.dataAccess import DataAccess

class Register:
   
    passwordDescription = None
    passwordContent = None
    id_user = 0

    def __init__(self, passwordDescription, passwordContent, id_user):
        self.passwordDescription = passwordDescription
        self.passwordContent = passwordContent
        self.id_user = id_user

    def save(self, id = 0):
        try:
            if (id == 0):
                DataAccess.executeStatement("INSERT INTO registers (passwordDescription, passwordContent, id_user) VALUES ('{}', '{}', {:d})"
                .format(self.passwordDescription, self.passwordContent, self.id_user))
            else:
                DataAccess.executeStatement("UPDATE registers SET passwordDescription = '{}', passwordContent = '{}', id_user = {:d} WHERE id = {:d}"
                .format(self.passwordDescription, self.passwordContent, self.id_user, id))

            return "success"

        except:
            return "fail to save or update password object"

    @staticmethod
    def delete(id = 0):
        try:
            DataAccess.executeStatement("DELETE FROM registers WHERE id = {:d}".format(id))
        
            return "success"
        except:
            return "fail"

    @staticmethod
    def queryRegister(condition = ""):
        try:
            data = DataAccess.queryStatement("*", "registers", condition)

            array = []
            for i in range(0, len(data), 1):
                password = {
                    "id": data[i][0],
                    "passwordDescription": data[i][1],
                    "passwordContent": data[i][2],
                    "id_user": data[i][3]
                }

                array.append(password)

            return array

        except:
            return "fail"

    @staticmethod
    def list(id = 0):
        if (id == 0):
            return Register.queryRegister(True)
        else:
            return Register.queryRegister("id = {:d}".format(id))
                

    @staticmethod
    def getRegisterByUser(user_id):
        return Register.queryRegister("id_user = {:d}".format(user_id))