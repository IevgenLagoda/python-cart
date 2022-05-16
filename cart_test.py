import unittest
from product import Product
from user import User
from productcart import ProductCart
from cart import Cart

class TestCart(unittest.TestCase):
    def test_add_product_to_cart(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        product1 = Product(1, 'test', 100)
        product2 = Product(2, 'test', 200)
        amount = 2
        discount = 10
        productcart = ProductCart(product2, amount, discount)
        cart.addProductToCart(product1, amount, discount)
        cart.addProductToCart(productcart)
        self.assertEqual(cart.getProductById(1), product1)
        self.assertEqual(cart.getProductById(2), product2)

    def test_is_user_valid(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        self.assertTrue(cart.isUserValid(), True)

    def test_is_user_auth_valid(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'den2001@ukr.net', 'qwerty'))
        login = 'den2001@ukr.net'
        password = 'qwerty'
        self.assertTrue(cart.isUserAuthValid(login, password), True)

    def test_get_total_cart_price(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        total_price = 170
        cart.addProductToCart(Product(1, 'test', 100), 1, 10)
        cart.addProductToCart(Product(2, 'test', 100), 1, 20)
        self.assertEqual(cart.getTotalCartPrice(), total_price)

    def test_get_total_discount(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        total_discount = 30
        cart.addProductToCart(Product(1, 'test', 100), 1, 10)
        cart.addProductToCart(Product(2, 'test', 100), 1, 20)
        self.assertEqual(cart.getTotalDicount(), total_discount)

    def test_is_cart_empty(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        self.assertTrue(cart.isCartEmpty(), True)

    def test_get_product_by_id(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        product = Product(1, 'test', 100)
        cart.addProductToCart(product)
        self.assertEqual(cart.getProductById(1), product)

    def test_remove_product_by_id(self):
        cart = Cart(User('test', 'test', 'test', 'test', 'test', 'test'))
        cart.addProductToCart(Product(1, 'test', 100), 2, 10)
        self.assertEqual(cart.products[1].getAmount(), 2)
        new_amount = 1
        cart.removeProductById(1, new_amount)
        self.assertEqual(cart.products[1].getAmount(), new_amount)
        new_amount = 2
        cart.removeProductById(1, new_amount)
        self.assertTrue(cart.isCartEmpty(), True)


unittest.main()