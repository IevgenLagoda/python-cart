import re

class User:
    def __init__(self, first_name, last_name, tel, address,  email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.address = address
        self.email = email
        self.password = password

    def getFullName(self):
        if self.isFullNameExists() == False:
            return ''
        return '{} {}'.format(self.first_name, self.last_name)

    def isFullNameExists(self):
        if len(self.first_name) == 0 or len(self.last_name) == 0:
            return False
        return True

    def setFullName(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

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

    def setPhoneNumber(self, tel):
        self.tel = tel

    def isUserDataExists(self):
        return self.isFullNameExists() and self.isPhoneNumberExists() and self.isAddressExists()

    def isEmailExists(self):
        return len(self.email) > 0

    def getEmail(self):
        if self.isEmailExists() == False:
            return ''
        return self.email

    def setEmail(self, email):
        self.email = email

    def isPasswordExists(self):
        return len(self.password) > 0

    def getPassword(self):
        if self.isPasswordExists() == False:
            return ''
        return self.password

    def setPassword(self, password):
        self.password = password

    def isPasswordStrong(self):
        password = self.getPassword()
        if len(password) < 6:
            raise 'The password must have 6 characters length'
        result = re.findall('(?=.*\d)(?=.*[a-z])(?=.*[A-Z])', password)
        if len(result) == 0:
            raise 'The password must have uppercase and lowercase Latin letters, one number'
        return True

    def canBeLogged(self, email, password):
        return self.getEmail() == email and self.getPassword() == password
