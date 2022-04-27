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

    def isAddressExists(self):
        return len(self.address) > 0

    def getAddress(self):
        if self.isAddressExists() == False:
            return ''
        return self.address

    def setAddress(self, address):
       self.address = address

    def isPhoneNumberExists(self):
        return len(self.tel) > 0

    def getPhoneNumber(self):
        if self.isPhoneNumberExists() == False:
            return ''
        return self.tel

    def isUserDataExists(self):
        return self.isFullNameExists() and self.isPhoneNumberExists() and self.isAddressExists()

    def isEmailExists(self):
        return len(self.email) > 0

    def getEmail(self):
        if self.isEmailExists() == False:
            return ''
        return self.email

    def isPasswordExists(self):
        return len(self.password) > 0

    def getPassword(self):
        if self.isPasswordExists() == False:
            return ''
        return self.password

    def canBeLogged(self, email, password):
        return self.getEmail() == email and self.getPassword() == password  # замена if на return, перемещение метода из класса Cart в класс UserAuth

