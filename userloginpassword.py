from user import User

class UserAuth(User): # переименование класса
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def isEmailExists(self):
        return len(self.email) > 0

    def isPasswordExists(self):
        return len(self.password) > 0

    def getEmail(self):
        if self.isEmailExists():
            return self.email
        return False

    def getPassword(self):
        if self.isPasswordExists():
            return self.password
        return False

    def canBeLogged(self, email, password):
        return self.getEmail() == email and self.getPassword() == password  # замена if на return, перемещение метода из класса Cart в класс UserAuth



