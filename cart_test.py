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
        # TODO: may we have productId1 and productId2 as consts?
        self.productId1 = 1
        self.productId2 = 2
        self.product1_amount = 1
        self.product2_amount = 2
        self.product1_discount = 10
        self.product2_discount = 20
        self.wrong_product_id = 3
        self.cart.addProductToCart(self.product1, 1, 10)
        self.cart.addProductToCart(self.product2, 2, 20)

    def test_add_product_to_cart(self):
        amount = 2
        discount = 10
        productcart = ProductCart(self.product2, amount, discount)
        self.cart.addProductToCart(self.product1, amount, discount)
        self.cart.addProductToCart(productcart)
        self.assertEqual(self.cart.getProductById(self.productId1), self.product1)
        self.assertEqual(self.cart.getProductById(self.productId2), self.product2)

    def test_is_user_valid(self):
        self.assertTrue(self.cart.isUserValid())
        cart = Cart(User('', '', '', '', 'test', 'test'))
        self.assertFalse(cart.isUserValid())

    def test_is_user_auth_valid(self):
        login = 'den2001@ukr.net'
        password = 'qwerty'
        self.assertTrue(self.cart.isUserAuthValid(login, password))
        wrong_login = 'den2000@ukr.net'
        self.assertFalse(self.cart.isUserAuthValid(wrong_login, password))
        wrong_password = 'qwert'
        self.assertFalse(self.cart.isUserAuthValid(login, wrong_password))

    def test_get_total_cart_price(self):
        product1_price = 100
        product2_price = 200
        total_price = (product1_price * self.product1_amount - self.product1_discount) + (
                    product2_price * self.product2_amount - self.product2_discount)
        self.assertEqual(self.cart.getTotalCartPrice(), total_price)
        self.cart.removeProductById(self.productId1, self.product1_amount)
        self.cart.removeProductById(self.productId2, self.product2_amount)
        empty_cart_total_price = 0
        self.assertEqual(self.cart.getTotalCartPrice(), empty_cart_total_price)

    def test_get_total_discount(self):
        product1_discount = 10
        product2_discount = 20
        total_discount = product1_discount + product2_discount
        self.assertEqual(self.cart.getTotalDicount(), total_discount)
        self.cart.removeProductById(self.productId1, self.product1_amount)
        self.cart.removeProductById(self.productId2, self.product2_amount)
        empty_cart_total_discount = 0
        self.assertEqual(self.cart.getTotalCartPrice(), empty_cart_total_discount)

    def test_is_cart_empty(self):
        self.assertFalse(self.cart.isCartEmpty())
        self.cart.removeProductById(self.productId1, self.product1_amount)
        self.cart.removeProductById(self.productId2, self.product2_amount)
        self.assertTrue(self.cart.isCartEmpty())

    def test_get_product_by_id(self):
        # TODO: please use const for the main value.
        self.assertEqual(self.cart.getProductById(self.productId1), self.product1)
        self.assertIsNone(self.cart.getProductById(self.wrong_product_id))

    def test_remove_product_by_id(self):
        self.assertEqual(self.cart.products[self.productId2].getAmount(), self.productId2)
        # TODO: let's rename it into something like `product_number``
        product_number = 1
        self.cart.removeProductById(self.productId2, product_number)
        self.assertEqual(self.cart.products[self.productId2].getAmount(), product_number)
        product_number = 2
        self.cart.removeProductById(self.productId2, product_number)
        self.assertFalse(self.cart.isCartEmpty())
        self.assertIsNone(self.cart.getProductById(self.productId2))


unittest.main()