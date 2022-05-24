import unittest
from product import Product
from user import User
from productcart import ProductCart
from cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart(User('test', 'test', 'test', 'test', 'den2001@ukr.net', 'qwerty'))
        self.product1 = Product(1, 'test', 100)
        self.product2 = Product(2, 'test', 200)
        self.cart.addProductToCart(self.product1, 1, 10)
        self.cart.addProductToCart(self.product2, 2, 20)

    def test_add_product_to_cart(self):
        # TODO: move general code into the setUp method. (this.cart)
        amount = 2
        discount = 10
        productcart = ProductCart(self.product2, amount, discount)
        self.cart.addProductToCart(self.product1, amount, discount)
        self.cart.addProductToCart(productcart)
        self.assertEqual(self.cart.getProductById(1), self.product1)
        self.assertEqual(self.cart.getProductById(2), self.product2)

    def test_is_user_valid(self):
        self.assertTrue(self.cart.isUserValid())
        cart = Cart(User('', '', '', '', 'test', 'test'))
        self.assertFalse(cart.isUserValid())
        # TODO: check for isUserValue(), False

    def test_is_user_auth_valid(self):
        # TODO: can we use the same consts for login and password here as well?
        login = 'den2001@ukr.net'
        password = 'qwerty'
        self.assertTrue(self.cart.isUserAuthValid(login, password))
        wrong_login = 'den2000@ukr.net'
        self.assertFalse(self.cart.isUserAuthValid(wrong_login, password))
        wrong_password = 'qwert'
        self.assertFalse(self.cart.isUserAuthValid(login, wrong_password))
        # TODO: check isUserAuthValid, False

    def test_get_total_cart_price(self):
        # TODO: would be good to calculate based on the price and other data.
        product1_price = 100
        product1_amount = 1
        product1_discount = 10
        product2_price = 200
        product2_amount = 2
        product2_discount = 20
        total_price = (product1_price * product1_amount - product1_discount) + (
                    product2_price * product2_amount - product2_discount)
        self.assertEqual(self.cart.getTotalCartPrice(), total_price)
        self.cart.removeProductById(1, 1)
        self.cart.removeProductById(2, 2)
        empty_cart_total_price = 0
        self.assertEqual(self.cart.getTotalCartPrice(), empty_cart_total_price)
        # TODO: to check for the empty cart as well.

    def test_get_total_discount(self):
        # TODO: to show how it's calculated.
        product1_discount = 10
        product2_discount = 20
        total_discount = product1_discount + product2_discount
        self.assertEqual(self.cart.getTotalDicount(), total_discount)
        self.cart.removeProductById(1, 1)
        self.cart.removeProductById(2, 2)
        empty_cart_total_discount = 0
        self.assertEqual(self.cart.getTotalCartPrice(), empty_cart_total_discount)
        # TODO: check for the empty cart.

    def test_is_cart_empty(self):
        self.assertFalse(self.cart.isCartEmpty())
        self.cart.removeProductById(1, 1)
        self.cart.removeProductById(2, 2)
        self.assertTrue(self.cart.isCartEmpty())
        # TODO: check for non empty cart as well.

    def test_get_product_by_id(self):
        # TODO: please use const for the main value.
        product_id = 1
        wrong_product_id = 3
        self.assertEqual(self.cart.getProductById(product_id), self.product1)
        self.assertIsNone(self.cart.getProductById(wrong_product_id))
        # TODO: check for wrong id.

    def test_remove_product_by_id(self):
        product_id = 2
        amount = 2
        self.assertEqual(self.cart.products[product_id].getAmount(), amount)
        new_amount = 1
        self.cart.removeProductById(product_id, new_amount)
        self.assertEqual(self.cart.products[product_id].getAmount(), new_amount)
        new_amount = 2
        self.cart.removeProductById(product_id, new_amount)
        # TODO: check the value from getAmount as well.
        self.assertFalse(self.cart.isCartEmpty())
        self.assertIsNone(self.cart.getProductById(product_id))


unittest.main()