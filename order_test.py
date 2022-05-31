import unittest
import filecmp
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
        self.delivery_status = 1
        self.order_filename = 'order.txt'
        self.filename_test = 'order_test.txt'
        self.filename_empty_list = 'order_test_empty_list.txt'

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
        # TODO: should be moved as const into the setup
        self.assertEqual(self.order.getDeliveryAddress(), self.delivery_address)

    def test_get_delivery_status(self):
        # TODO: should be moved as const into the setup
        self.assertEqual(self.order.getDeliveryStatus(), self.delivery_status)

    def test_get_order_user_data(self):
        # TODO: please use consts when possible.
        user_data_list = self.getUserData(self.cartUser)
        self.assertEqual(self.order.getOrderUserData(), user_data_list)

    def test_get_order_products_data(self):
        # TODO: please use consts when possible.
        # TODO: it's fine to use additional method in tests. getProductData(product)
        # TODO: it should be something like:
        # TODO:  products_data_list = [getProductData(self.product1), getProductData(self.product2)]
        products_data_list = [self.getProductData(self.productcart1), self.getProductData(self.productcart2)]
        self.assertEqual(self.order.getOrderProductsData(), products_data_list)

    def test_write_order_to_file(self):
        # TODO: to add const for the filename: order.txt
        self.order.exportToFile(self.order_filename)
        self.assertTrue(filecmp.cmp(self.order_filename, self.filename_test, shallow=False), True)
        self.order.writeListToFile([], self.order_filename)
        self.assertTrue(filecmp.cmp(self.order_filename, self.filename_empty_list, shallow=False), True)
        with self.assertRaises(IOError):
            self.order.exportToFile('')

unittest.main()