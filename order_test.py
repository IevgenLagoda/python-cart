import unittest
import filecmp

import order
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
        self.product1_price = 100
        self.product1_amount = 1
        self.product1_discount = 10
        self.product2_price = 200
        self.product2_amount = 2
        self.product2_discount = 20
        self.empty_cart_amount = 0
        self.empty_cart_discount = 0
        self.delivery_address = 'Fesenko1'
        self.delivery_status_new = 1
        self.delivery_status_order_processing = 2
        self.delivery_status_delivery = 3
        self.delivery_status_received = 4
        self.empty_products_list = []
        self.new_total_price = 940
        self.order_filename = 'order.txt'
        self.order_filename_etalon = 'order_test.txt'
        self.filename_empty_list_test = 'order_test_empty_list.txt'
        self.filename_empty_products_data = 'empty_products_data.txt'
        self.filename_wrong_user_data = 'wrong_user_data.txt'
        self.filename_new_data_order = 'new_data_order.txt'
        self.filename_data_order_after_test = 'data_order_after_test.txt'

    def getProductData(self, product):
        product_data = '{}|{}|{}|{}'.format(product.getName(), product.getPrice(),
                                            product.getAmount(), product.getDiscount())
        return product_data

    def getUserData(self, user):
        data_list = [user.getFullName(), user.getAddress(), user.getPhoneNumber(), user.getEmail()]
        return data_list

    def test_get_order_amount(self):
        product1 = Product(1, 'test1', 100)
        product2 = Product(2, 'test2', 200)
        productcart = ProductCart(product1, 1, 10)
        order_amount = (self.product1_price * self.product1_amount - self.product1_discount) + (
                self.product2_price * self.product2_amount - self.product2_discount)
        order = Order(self.cartUser, [productcart, (product2, 2, 20)], OrderStatus.new)
        self.assertEqual(order.getOrderAmount(), order_amount)
        order = Order(self.cartUser, [], OrderStatus.new)
        self.assertEqual(order.getOrderAmount(), self.empty_cart_amount)
        
    def test_get_order_discount(self):
        order_discount = self.product1_discount + self.product2_discount
        self.assertEqual(self.order.getOrderDicount(), order_discount)
        order = Order(self.cartUser, [], OrderStatus.new)
        self.assertEqual(order.getOrderDicount(), self.empty_cart_discount)

    def test_get_delivery_address(self):
        self.assertEqual(self.order.getDeliveryAddress(), self.delivery_address)

    def test_set_delivery_status(self):
        self.assertEqual(self.order.getDeliveryStatus(), self.delivery_status_new)
        self.order.setDeliveryStatus()
        self.assertEqual(self.order.getDeliveryStatus(), self.delivery_status_order_processing)
        self.order.setDeliveryStatus()
        self.assertEqual(self.order.getDeliveryStatus(), self.delivery_status_delivery)
        self.order.setDeliveryStatus()
        self.assertEqual(self.order.getDeliveryStatus(), self.delivery_status_received)
        self.order.setDeliveryStatus()
        self.assertEqual(self.order.getDeliveryStatus(), self.delivery_status_received)

    def test_get_order_user_data(self):
        user_data_list = self.getUserData(self.cartUser)
        self.assertEqual(self.order.getOrderUserData(), user_data_list)

    def test_get_order_products_data(self):
        products_data_list = [self.getProductData(self.productcart1), self.getProductData(self.productcart2)]
        self.assertEqual(self.order.getOrderProductsData(), products_data_list)

    def test_write_order_to_file(self):
        self.order.exportToFile(self.order_filename)
        self.assertTrue(filecmp.cmp(self.order_filename, self.order_filename_etalon, shallow=False), True)
        self.order.writeListToFile(self.empty_products_list, self.order_filename)
        self.assertTrue(filecmp.cmp(self.order_filename, self.filename_empty_list_test, shallow=False), True)
        with self.assertRaises(IOError):
            self.order.exportToFile('')

    def test_get_order_from_file(self):
        test_order = self.order.getOrderFromFile(self.order_filename_etalon)
        test_order.exportToFile(self.order_filename)
        self.assertTrue(filecmp.cmp(self.order_filename_etalon, self.order_filename, shallow=False), True)
        test_order = self.order.getOrderFromFile(self.filename_empty_products_data)
        self.assertEqual(self.empty_products_list, test_order.getOrderProductsData())
        test_order = self.order.getOrderFromFile(self.filename_wrong_user_data)
        self.assertFalse(test_order.user.isFullNameExists())
        self.assertFalse(test_order.user.isPhoneNumberExists())
        self.assertFalse(test_order.user.isAddressExists())
        self.assertFalse(test_order.user.isEmailExists())
        with self.assertRaises(Exception):
            self.order.getOrderFromFile(self.filename_empty_list_test)
        with self.assertRaises(IOError):
            self.order.getOrderFromFile('')

    def test_get_data_from_file(self):
        self.order.getDataFromFile(self.filename_new_data_order)
        self.order.exportToFile(self.order_filename)
        self.assertTrue(filecmp.cmp(self.filename_data_order_after_test, self.order_filename, shallow=False), True)
        self.order.getDataFromFile(self.filename_empty_products_data)
        self.assertEqual(self.order.cart.getTotalCartPrice(), self.new_total_price)
        self.order.getDataFromFile(self.filename_wrong_user_data)
        self.assertFalse(self.order.user.isFullNameExists())
        self.assertFalse(self.order.user.isPhoneNumberExists())
        self.assertFalse(self.order.user.isAddressExists())
        self.assertFalse(self.order.user.isEmailExists())

        with self.assertRaises(Exception):
            self.order.getDataFromFile(self.filename_empty_list_test)
        with self.assertRaises(IOError):
            self.order.getDataFromFile('')


unittest.main()