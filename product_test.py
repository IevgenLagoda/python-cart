import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_init_data(self):
        id = 1
        name = 'test'
        price = 100
        product = Product(id, name, price)
        self.assertEqual(product.getId(), id)
        self.assertEqual(product.getName(), name)
        self.assertEqual(product.getPrice(), price)

unittest.main()