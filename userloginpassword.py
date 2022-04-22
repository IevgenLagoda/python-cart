from user import User

class UserLoginPassword(User):
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def isLoginExist(self):
        if len(self.login) == 0:
            return False
        return True

    def isPasswordExist(self):
        if len(self.password) == 0:
            return False
        return True

    def getLogin(self):
        if self.isLoginExist():
            return self.login
        return False

    def getPassword(self):
        if self.isPasswordExist():
            return self.password
        return False



