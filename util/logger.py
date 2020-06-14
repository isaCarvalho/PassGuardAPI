from datetime import datetime

class Logger:

    @staticmethod
    def log(message = ""):
        file_name = "log-{}.txt".format(datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))

        file = open("logs/{}".format(file_name), "w")
        file.write("{}".format(message))
        file.close()
