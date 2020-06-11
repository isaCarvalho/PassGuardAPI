from dao.dataAccess import DataAccess

class User:
  
    name = None
    email = None
    password = None

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save(self, id = 0):
        try:
            if (id == 0):
                DataAccess.executeStatement("INSERT INTO users (name, email, password) VALUES ('{}', '{}', '{}')"
                .format(self.name, self.email, self.password))
            else:
                DataAccess.executeStatement("UPDATE users SET name = '{}', password = '{}', email = '{}' WHERE id = {:d}"
                .format(self.name, self.password, self.email, id))
            
            return "success"

        except:
            return "fail to save or update user"

    @staticmethod
    def delete(id):
        try:
            DataAccess.executeStatement("DELETE FROM users WHERE id = {:d}".format(id))
        
            return "success"
        except:
            return "fail"

    @staticmethod
    def list(id = 0):
        try:
            if (id == 0):
                data = DataAccess.queryStatement("*", "users")
            else:
                data = DataAccess.queryStatement("*", "users", "id = {:d}".format(id))

            array = []
            for i in range(0, len(data), 1):
                user = {
                    "id": data[i][0],
                    "username": data[i][1],
                    "email": data[i][2],
                    "password": data[i][3]
                }

                array.append(user)

            return array

        except:
            return "fail"