import unittest
from product import Product
from productcart import ProductCart

class TestProductCart(unittest.TestCase):
    def test_get_data(self):
        product = Product(1, 'test', 100)
        amount = 2
        discount = 20
        total_price = 180
        productcart = ProductCart(product, amount, discount)
        self.assertEqual(productcart.getProduct(), product)
        # TODO: to use constants as 2nd params.
        self.assertEqual(productcart.getAmount(), 2)
        self.assertEqual(productcart.getDiscount(), 20)
        # TODO: to use total_price as 2nd pram?
        self.assertEqual(productcart.getProductTotalPrice(), 180)

    def test_set_data(self):
        productcart = ProductCart(Product(1, 'test', 100), 2, 20)
        new_amount = 3
        new_discount = 10
        # TODO: to check for the old values first.
        productcart.setAmount(new_amount)
        productcart.setDiscount(new_discount)
        self.assertEqual(productcart.getAmount(), 3)
        self.assertEqual(productcart.getDiscount(), 10)

unittest.main()
