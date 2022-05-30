import unittest
import filecmp
import os
from user import User
from product import Product
from productcart import ProductCart
from order import Order, OrderStatus

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.cartUser = User('Den', 'Vasin', '0503616655', 'Fesenko1', 'den2001@ukr.net', 'qwerty')
        self.productcart1 = ProductCart(Product(1, 'test1', 100), 1, 10)
        self.productcart2 = ProductCart(Product(2, 'test2', 200), 2, 20)
        self.order = Order(self.cartUser, [self.productcart1, self.productcart2], OrderStatus.new)

    def test_get_order_amount(self):
        product1 = Product(1, 'test1', 100)
        product2 = Product(2, 'test2', 200)
        productcart = ProductCart(product1, 1, 10)
        product1_price = 100
        product1_amount = 1
        product1_discount = 10
        product2_price = 200
        product2_amount = 2
        product2_discount = 20
        order_amount = (product1_price * product1_amount - product1_discount) + (product2_price * product2_amount - product2_discount)
        order = Order(self.cartUser, [productcart, (product2, 2, 20)], OrderStatus.new)
        self.assertEqual(order.getOrderAmount(), order_amount)
        order = Order(self.cartUser, [], OrderStatus.new)
        empty_cart_amount = 0
        self.assertEqual(order.getOrderAmount(), empty_cart_amount)
        
    def test_get_order_discount(self):
        product1_discount = 10
        product2_discount = 20
        order_discount = product1_discount + product2_discount
        self.assertEqual(self.order.getOrderDicount(), order_discount)
        order = Order(self.cartUser, [], OrderStatus.new)
        empty_cart_discount = 0
        self.assertEqual(order.getOrderDicount(), empty_cart_discount)

    def test_get_delivery_address(self):
        # TODO: should be moved as const into the setup
        delivery_address = 'Fesenko1'
        self.assertEqual(self.order.getDeliveryAddress(), delivery_address)

    def test_get_delivery_status(self):
        # TODO: should be moved as const into the setup
        delivery_status = 1
        self.assertEqual(self.order.getDeliveryStatus(), delivery_status)

    def test_get_order_user_data(self):
        # TODO: please use consts when possible.
        user_data_list = ['Den Vasin', 'Fesenko1', '0503616655', 'den2001@ukr.net']
        self.assertEqual(self.order.getOrderUserData(), user_data_list)

    def test_get_order_products_data(self):
        # TODO: please use consts when possible.
        # TODO: it's fine to use additional method in tests. getProductData(product)
        # TODO: it should be something like:
        # TODO:  products_data_list = [getProductData(self.product1), getProductData(self.product2)]
        products_data_list = ['test1|100|1|10', 'test2|200|2|20']
        self.assertEqual(self.order.getOrderProductsData(), products_data_list)

    def test_write_order_to_file(self):
        # TODO: to add const for the filename: order.txt
        self.order.exportToFile('order.txt')
        self.assertTrue(filecmp.cmp('order.txt', 'order_test.txt', shallow=False), True)
        self.order.writeListToFile([], 'order.txt')
        self.assertTrue(filecmp.cmp('order.txt', 'order_test_empty_list.txt', shallow=False), True)
        with self.assertRaises(IOError):
            self.order.exportToFile('')

unittest.main()