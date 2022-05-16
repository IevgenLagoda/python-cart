import unittest
from product import Product
from productcart import ProductCart

class TestProductCart(unittest.TestCase):
    def test_get_product(self):
        product = Product(1, 'test', 100)
        productcart = ProductCart(product,  2, 20)
        # TODO: to use constants as 2nd params.
        self.assertEqual(productcart.getProduct(), product)

    def test_get_amount(self):
        amount = 2
        productcart = ProductCart(Product(1, 'test', 100), amount, 20)
        self.assertEqual(productcart.getAmount(), amount)

    def test_get_discount(self):
        discount = 20
        productcart = ProductCart(Product (1, 'test', 100), 2, discount)
        self.assertEqual(productcart.getDiscount(), discount)

    def test_get_totalprice(self):
        total_price = 180
        productcart = ProductCart (Product (1, 'test', 100), 2, 20)
        # TODO: to use total_price as 2nd pram?
        self.assertEqual(productcart.getProductTotalPrice(), total_price)

    def test_set_amount(self):
        productcart = ProductCart(Product(1, 'test', 100), 2, 20)
        new_amount = 3
        # TODO: to check for the old values first.
        self.assertEqual (productcart.getAmount(), 2)
        productcart.setAmount(new_amount)
        self.assertEqual(productcart.getAmount(), new_amount)

    def test_set_discount(self):
        productcart = ProductCart (Product (1, 'test', 100), 2, 20)
        new_discount = 10
        self.assertEqual (productcart.getDiscount(), 20)
        productcart.setDiscount(new_discount)
        self.assertEqual(productcart.getDiscount(), new_discount)

unittest.main()
