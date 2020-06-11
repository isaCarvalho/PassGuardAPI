from dao.dataAccess import DataAccess

class Password:
   
    passwordDescription = None
    passwordContent = None

    def __init__(passwordDescription, passwordContent):
        self.passwordDescription = passwordDescription
        self.passwordContent = passwordContent

    def save(self, id = 0):
        try:
            if (id == 0):
                DataAccess.executeStatement("INSERT INTO registers (passwordDescription, passwordContent) VALUES ('{}', '{}')"
                .format(self.passwordDescription, self.passwordContent))
            else:
                DataAccess.executeStatement("UPDATE registers SET passwordDescription = '{}', passwordContent = '{}' WHERE id = {:d}"
                .format(self.passwordDescription, self.passwordContent, id))

        except:
            print("fail to save or update password object")

    @staticmethod
    def delete(id = 0):
        try:
            DataAccess.executeStatement("DELETE FROM registers WHERE id = {:d}".format(id))
        
            return "success"
        except:
            return "fail"

    @staticmethod
    def list(id = 0):
        try:
            if (id == 0):
                data = DataAccess.queryStatement("*", "registers")
            else:
                data = DataAccess.queryStatement("*", "registers", "id = {:d}".format(id))
                
            array = []
            for i in range(0, len(data), 1):
                password = {
                    "id": data[i][0],
                    "passwordDescription": data[i][1],
                    "passwordContent": data[i][2]
                }

                array.append(password)

            return array

        except:
            return "fail"