import unittest
from product import Product
from productcart import ProductCart

class TestProductCart(unittest.TestCase):
    def setUp(self):
        self.productcart = ProductCart(Product(1, 'test', 100), 2, 20)
        self.product_price = 100
        self.product_amount = 2
        self.product_dicount = 20
        self.new_amount = 3
        self.new_discount = 10

    def test_get_product(self):
        product = Product(1, 'test', 100)
        productcart = ProductCart(product, self.product_amount, self.product_dicount)
        self.assertEqual(productcart.getProduct(), product)

    def test_get_amount(self):
        # TODO: amount should be const in setup and then we don't need new instance.
        self.assertEqual(self.productcart.getAmount(), self.product_amount)

    def test_get_discount(self):
        # TODO: discount should be const in setup and then we don't need new instance.
        self.assertEqual(self.productcart.getDiscount(), self.product_dicount)

    def test_get_total_price(self):
        total_price = self.product_price * self.product_amount - self.product_dicount
        self.assertEqual(self.productcart.getProductTotalPrice(), total_price)

    def test_set_amount(self):
        # TODO: 2 should be a const.
        self.assertEqual(self.productcart.getAmount(), self.product_amount)
        self.productcart.setAmount(self.new_amount)
        self.assertEqual(self.productcart.getAmount(), self.new_amount)

    def test_set_discount(self):
        self.assertEqual(self.productcart.getDiscount(), self.product_dicount)
        self.productcart.setDiscount(self.new_discount)
        self.assertEqual(self.productcart.getDiscount(), self.new_discount)

unittest.main()
