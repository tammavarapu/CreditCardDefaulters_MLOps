from datetime import datetime


class CustomAppLogger:

    def __init__(self):
        pass

    def log(self, fileObject, message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.currentTime = self.now.strftime('%H:%M:%S')
        fileObject.write(
            str(self.date) + "/" + str(self.currentTime) + "\t\t" + message + "\n" )