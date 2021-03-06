import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.first_name = 'Den'
        self.last_name = 'Vasin'
        self.address = 'Fesenko1'
        self.phone_number = '0503616655'
        self.email = 'den2001@ukr.net'
        self.password = 'Qwerty5'
        self.empty_first_name = ''
        self.empty_last_name = ''
        self.empty_address = ''
        self.empty_phone_number = ''
        self.empty_email = ''
        self.empty_password = ''
        self.new_address = 'Fesenko2'
        self.password_lower_symbols = 'qwerty5'
        self.password_upper_symbols = 'QWERTY5'
        self.password_only_numbers = '555555'
        self.password_without_number = 'Qwertyy'
        self.password_less_6_chars = 'Qwet6'
        self.full_name = '{} {}'.format (self.first_name, self.last_name)
        self.user = User(self.first_name, self.last_name, self.phone_number, self.address, self.email, self.password)

    def test_get_full_name(self):
        self.assertEqual(self.user.getFullName(), self.full_name)

    def test_is_full_name_exists(self):
        self.assertTrue(self.user.isFullNameExists())
        self.user.setFullName(self.empty_first_name, self.empty_last_name)
        self.assertFalse(self.user.isFullNameExists())

    def test_is_address_exists(self):
        self.assertTrue(self.user.isAddressExists())
        self.user.setAddress(self.empty_address)
        self.assertFalse(self.user.isAddressExists())

    def test_set_address(self):
        self.assertEqual(self.user.getAddress(), self.address)
        self.user.setAddress(self.new_address)
        self.assertEqual(self.user.getAddress(), self.new_address)

    def test_is_phone_number_exists(self):
        self.assertTrue(self.user.isPhoneNumberExists())
        self.user.setPhoneNumber(self.empty_phone_number)
        self.assertFalse(self.user.isPhoneNumberExists())

    def test_get_phone_number(self):
        self.assertEqual(self.user.getPhoneNumber(), self.phone_number)

    def test_is_user_data_exists(self):
        self.assertTrue(self.user.isUserDataExists())
        self.user.setFullName(self.empty_first_name, self.empty_last_name)
        self.user.setPhoneNumber(self.empty_phone_number)
        self.user.setAddress(self.empty_address)
        self.assertFalse(self.user.isUserDataExists())

    def test_is_email_exists(self):
        self.assertTrue(self.user.isEmailExists())
        self.user.setEmail(self.empty_email)
        self.assertFalse(self.user.isEmailExists())

    def test_get_email(self):
        self.assertEqual(self.user.getEmail(), self.email)

    def test_is_password_exists(self):
       self.assertTrue(self.user.isPasswordExists())
       self.user.setPassword(self.empty_password)
       self.assertFalse(self.user.isPasswordExists())

    def test_get_password(self):
        self.assertEqual(self.user.getPassword(), self.password)

    def test_is_password_stong(self):
        self.assertTrue(self.user.isPasswordStrong())
        self.user.setPassword(self.empty_password)
        with self.assertRaises(Exception):
            self.assertTrue(self.user.isPasswordStrong())
        self.user.setPassword(self.password_lower_symbols)
        with self.assertRaises(Exception):
            self.assertTrue(self.user.isPasswordStrong())
        self.user.setPassword(self.password_upper_symbols)
        with self.assertRaises(Exception):
            self.assertTrue(self.user.isPasswordStrong())
        self.user.setPassword(self.password_only_numbers)
        with self.assertRaises(Exception):
            self.assertTrue(self.user.isPasswordStrong())
        self.user.setPassword(self.password_without_number)
        with self.assertRaises(Exception):
            self.assertTrue(self.user.isPasswordStrong())
        self.user.setPassword(self.password_less_6_chars)
        with self.assertRaises(Exception):
            self.assertTrue(self.user.isPasswordStrong())

    def test_can_be_logged(self):
        self.assertTrue(self.user.canBeLogged(self.email, self.password))
        self.assertFalse(self.user.canBeLogged(self.empty_email, self.empty_password))

unittest.main()