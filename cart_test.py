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
        cart = Cart(User('test', 'test', 'test', 'test', '', ''))
        self.assertFalse(cart.isUserValid())
        # TODO: check for isUserValue(), False

    def test_is_user_auth_valid(self):
        # TODO: can we use the same consts for login and password here as well?
        login = 'den2001@ukr.net'
        password = 'qwerty'
        self.assertTrue(self.cart.isUserAuthValid(login, password))
        wrong_login = 'den2001@ukr.net'
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
        product2_amount = 1
        product2_discount = 20
        total_price = (product1_price * product1_amount - product1_discount) + (
                    product2_price * product2_amount - product2_discount)
        self.cart.addProductToCart(self.product1, 1, 10)
        self.cart.addProductToCart(self.product2, 1, 20)
        self.assertEqual(self.cart.getTotalCartPrice(), total_price)
        # TODO: to check for the empty cart as well.

    def test_get_total_discount(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        # TODO: to show how it's calculated.
        total_discount = 30
        cart.addProductToCart(Product(1, 'test', 100), 1, 10)
        cart.addProductToCart(Product(2, 'test', 100), 1, 20)
        self.assertEqual(cart.getTotalDicount(), total_discount)
        # TODO: check for the empty cart.

    def test_is_cart_empty(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        self.assertTrue(cart.isCartEmpty(), True)
        # TODO: check for non empty cart as well.

    def test_get_product_by_id(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        # TODO: please use const for the main value.
        product = Product(1, 'test', 100)
        cart.addProductToCart(product)
        self.assertEqual(cart.getProductById(1), product)
        # TODO: check for wrong id.

    def test_remove_product_by_id(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        cart.addProductToCart(Product(1, 'test', 100), 2, 10)
        self.assertEqual(cart.products[1].getAmount(), 2)
        new_amount = 1
        cart.removeProductById(1, new_amount)
        self.assertEqual(cart.products[1].getAmount(), new_amount)
        new_amount = 2
        cart.removeProductById(1, new_amount)
        # TODO: check the value from getAmount as well.
        self.assertTrue(cart.isCartEmpty(), True)


unittest.main()