class User:

    def __init__(self, first_name, last_name, tel, address,  email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.address = address
        self.email = email
        self.password = password

    def getFullName(self):
        if self.isFullNameExists():
            return ''
        return '{} {}'.format(self.first_name, self.last_name)

    def isFullNameExists(self):
        if len(self.first_name) == 0 or len(self.last_name) == 0:
            return False
        return True

    def getAddress(self):
        if self.isAddressExists():
            return ''
        return self.address

    def isAddressExists(self):
        if len(self.address) == 0:
            return False
        return True

    def setAddress(self, address):
       self.address = address

    def getPhoneNumber(self):
        if self.isPhoneNumberExists():
            return self.tel
        return ''

    def isPhoneNumberExists(self):
        if len(self.tel) == 0:
            return False
        return True

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

