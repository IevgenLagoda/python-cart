import unittest
import filecmp
import os.path
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
        # TODO: move common code into the setUp method.
        product1 = Product(1, 'test1', 100)
        product2 = Product(2, 'test2', 200)
        productcart = ProductCart(product1, 1, 10)
        # TODO: how 470 is calculated.
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
        # TODO: to check for an empty order.

    def test_get_order_discount(self):
        # TODO: how it's calculated?
        product1_discount = 10
        product2_discount = 20
        order_discount = product1_discount + product2_discount
        self.assertEqual(self.order.getOrderDicount(), order_discount)
        order = Order(self.cartUser, [], OrderStatus.new)
        empty_cart_discount = 0
        self.assertEqual(order.getOrderDicount(), empty_cart_discount)
        # TODO: to check for an empty order.

    def test_get_delivery_address(self):
        delivery_address = 'Fesenko1'
        self.assertEqual(self.order.getDeliveryAddress(), delivery_address)

    def test_get_delivery_status(self):
        delivery_status = 1
        self.assertEqual(self.order.getDeliveryStatus(), delivery_status)

    def test_get_order_user_data(self):
        # TODO: please use consts when possible.
        user_data_list = ['Den Vasin', 'Fesenko1', '0503616655', 'den2001@ukr.net']
        self.assertEqual(self.order.getOrderUserData(), user_data_list)

    def test_get_order_products_data(self):
        products_data_list = ['test1|100|1|10', 'test2|200|2|20']
        self.assertEqual(self.order.getOrderProductsData(), products_data_list)

    def test_write_order_to_file(self):
        self.order.exportToFile('order.txt')
        self.assertTrue(filecmp.cmp('order.txt', 'order_test.txt', shallow=False), True)
        self.order.writeListToFile([], 'order.txt')
        file_size_empty_list_write = 0
        self.assertEqual(os.path.getsize('/Code/Project/Cart/order.txt'), file_size_empty_list_write)


        # TODO: writeListToFile should be tested as well for exaptions and empty list.
    def test_file_exp(self):
        file = open('order.txt', 'w')
        #with self.assertRaises(IOError):
           #self.order.exportToFile('order.txt')
        file.close()

unittest.main()