import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.first_name = 'Den'
        self.last_name = 'Vasin'
        self.address = 'Fesenko1'
        self.phone_number = '0503616655'
        self.email = 'den2001@ukr.net'
        self.password = 'qwerty'
        self.empty_first_name = ''
        self.empty_last_name = ''
        self.empty_address = ''
        self.empty_phone_number = ''
        self.empty_email = ''
        self.empty_password = ''

    def test_get_full_name(self):
        # TODO: move common code into the setUp method.
        user = User(self.first_name, self.last_name, 'tel', 'address', 'email', 'password')
        full_name = '{} {}'.format(self.first_name, self.last_name)
        self.assertEqual(user.getFullName(), full_name)

    def test_is_full_name_exists(self):
        user = User(self.first_name, self.last_name, 'tel', 'address', 'email', 'password')
        self.assertTrue(user.isFullNameExists())
        # TODO: instead of new isntance would be good to set emopty name and check.
        # TODO: - maybe it will require a new method setName(first_name, last_name)
        user = User(self.empty_first_name, self.empty_last_name, 'tel', 'address', 'email', 'password')
        self.assertFalse(user.isFullNameExists())

    def test_is_address_exists(self):
        user = User('first_name', 'last_name', 'tel', self.address, 'email', 'password')
        self.assertTrue(user.isAddressExists())
        user = User('first_name', 'last_name', 'tel', self.empty_address, 'email', 'password')
        self.assertFalse(user.isAddressExists())

    # TODO: it's fine to have name only with `set` - test_set_address()
    def test_get_set_address(self):
        user = User('first_name', 'last_name', 'tel', self.address, 'email', 'password')
        self.assertEqual(user.getAddress(), self.address)
        new_address = 'Fesenko2'
        user.setAddress(new_address)
        self.assertEqual(user.getAddress(), new_address)

    def test_is_phone_number_exists(self):
        user = User('first_name', 'last_name', self.phone_number, 'address', 'email', 'password')
        self.assertTrue(user.isPhoneNumberExists())
        user = User('first_name', 'last_name', self.empty_phone_number, 'address', 'email', 'password')
        self.assertFalse(user.isPhoneNumberExists())

    def test_get_phone_number(self):
        user = User('first_name', 'last_name', self.phone_number, 'address', 'email', 'password')
        self.assertEqual(user.getPhoneNumber(), self.phone_number)

    def test_is_user_data_exists(self):
        user = User(self.first_name, self.last_name, self.phone_number, self.address, 'email', 'password')
        self.assertTrue(user.isUserDataExists())
        user = User(self.empty_first_name, self.empty_last_name, self.phone_number, self.empty_address, 'email', 'password')
        self.assertFalse(user.isUserDataExists())

    def test_is_email_exists(self):
        user = User('first_name', 'last_name', 'phone_number', 'address', self.email, 'password')
        self.assertTrue(user.isEmailExists())
        user = User('first_name', 'last_name', 'phone_number', 'address', self.empty_email, 'password')
        self.assertFalse(user.isEmailExists())

    def test_get_email(self):
        user = User('first_name', 'last_name', 'phone_number', 'address', self.email, 'password')
        self.assertEqual(user.getEmail(), self.email)

    def test_is_password_exists(self):
        user = User('first_name', 'last_name', 'phone_number', 'address', 'email', self.password)
        self.assertTrue(user.isPasswordExists())
        user = User('first_name', 'last_name', 'phone_number', 'address', 'email', self.empty_password)
        self.assertFalse(user.isPasswordExists())

    def test_get_password(self):
        user = User('first_name', 'last_name', 'phone_number', 'address', 'email', self.password)
        self.assertEqual(user.getPassword(), self.password)

    def test_can_be_logged(self):
        user = User('first_name', 'last_name', 'phone_number', 'address', self.email, self.password)
        self.assertTrue(user.canBeLogged(self.email, self.password))
        self.assertFalse(user.canBeLogged(self.empty_email, self.empty_password))

# TODO: add test for `isPasswordStrong``
unittest.main()