import unittest
from user import User

class TestUser(unittest.TestCase):
    def test_get_full_name(self):
        first_name = 'Den'
        last_name = 'Vasin'
        user = User(first_name, last_name, 'tel', 'address', 'email', 'password')
        self.assertEqual(user.getFullName(), '{} {}'.format(first_name, last_name))

    def test_is_full_name_exists(self):
        first_name = 'Den'
        last_name = 'Vasin'
        user = User(first_name, last_name, 'tel', 'address', 'email', 'password')
        self.assertTrue(user.isFullNameExists(), True)

    def test_is_address_exists(self):
        address = 'Fesenko1'
        user = User('first_name', 'last_name', 'tel', address, 'email', 'password')
        self.assertTrue(user.isAddressExists(), True)

    def test_get_address(self):
        address = 'Fesenko1'
        user = User('first_name', 'last_name', 'tel', address, 'email', 'password')
        self.assertEqual(user.getAddress(), address)

    def test_set_address(self):
        user = User('first_name', 'last_name', 'tel', 'Fesenko1', 'email', 'password')
        new_address = 'Fesenko2'
        self.assertEqual (user.getAddress (), 'Fesenko1')
        user.setAddress(new_address)
        self.assertEqual (user.getAddress (), new_address)

    def test_is_phone_number_exists(self):
        phone_number = '0503616655'
        user = User('first_name', 'last_name', phone_number, 'address', 'email', 'password')
        self.assertTrue(user.isPhoneNumberExists(), True)

    def test_get_phone_number(self):
        phone_number = '0503616655'
        user = User('first_name', 'last_name', phone_number, 'address', 'email', 'password')
        self.assertEqual(user.getPhoneNumber(), phone_number)

    def test_is_user_data_exists(self):
        user = User('Den', 'Vasin', '0503616655', 'Fesenko2', 'email', 'password')
        self.assertEqual(user.isUserDataExists(), True)

    def test_is_email_exists(self):
        email = 'den2001@ukr.net'
        user = User('first_name', 'last_name', 'phone_number', 'address', email, 'password')
        self.assertTrue(user.isAddressExists(), True)

    def test_get_email(self):
        email = 'den2001@ukr.net'
        user = User('first_name', 'last_name', 'phone_number', 'address', email, 'password')
        self.assertEqual(user.getEmail(), email)

    def test_is_password_exists(self):
        password = 'qwerty'
        user = User ('first_name', 'last_name', 'phone_number', 'address', 'email', password)
        self.assertTrue(user.isPasswordExists(), True)

    def test_get_password(self):
        password = 'qwerty'
        user = User('first_name', 'last_name', 'phone_number', 'address', 'email', password)
        self.assertEqual(user.getPassword(), password)

    def test_can_be_logged(self):
        email = 'den2001@ukr.net'
        password = 'qwerty'
        user = User ('first_name', 'last_name', 'phone_number', 'address', 'den2001@ukr.net', 'qwerty')
        self.assertTrue(user.canBeLogged(email, password), True)


unittest.main()