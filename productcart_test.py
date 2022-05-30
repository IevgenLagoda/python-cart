import unittest
from product import Product
from productcart import ProductCart

class TestProductCart(unittest.TestCase):
    def setUp(self):
        self.productcart = ProductCart(Product(1, 'test', 100), 2, 20)

    def test_get_product(self):
        product = Product(1, 'test', 100)
        productcart = ProductCart(product,  2, 20)
        self.assertEqual(productcart.getProduct(), product)

    def test_get_amount(self):
        # TODO: amount should be const in setup and then we don't need new instance.
        amount = 2
        productcart = ProductCart(Product(1, 'test', 100), amount, 20)
        self.assertEqual(productcart.getAmount(), amount)

    def test_get_discount(self):
        # TODO: discount should be const in setup and then we don't need new instance.
        discount = 20
        productcart = ProductCart(Product(1, 'test', 100), 2, discount)
        self.assertEqual(productcart.getDiscount(), discount)

    def test_get_total_price(self):
        product_price = 100
        product_amount = 2
        product_dicount = 20
        total_price = product_price * product_amount - product_dicount
        self.assertEqual(self.productcart.getProductTotalPrice(), total_price)

    def test_set_amount(self):
        new_amount = 3
        # TODO: 2 should be a const.
        self.assertEqual(self.productcart.getAmount(), 2)
        self.productcart.setAmount(new_amount)
        self.assertEqual(self.productcart.getAmount(), new_amount)

    def test_set_discount(self):
        new_discount = 10
        self.assertEqual(self.productcart.getDiscount(), 20)
        self.productcart.setDiscount(new_discount)
        self.assertEqual(self.productcart.getDiscount(), new_discount)

unittest.main()
