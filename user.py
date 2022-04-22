class User:

    def __init__(self, first_name, last_name, tel, address):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.address = address

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

