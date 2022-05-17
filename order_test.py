import unittest
from user import User
from product import Product
from productcart import ProductCart
from order import Order, OrderStatus

class TestOrder(unittest.TestCase):
    def test_get_order_amount(self):
        cartUser = User('first_name', 'last_name', 'phone_number', 'address', 'email', 'password')
        product1 = Product(1, 'test1', 100)
        product2 = Product(2, 'test2', 200)
        productcart = ProductCart(product1, 1, 10)
        order_amount = 470
        order = Order(cartUser, [productcart, (product2, 2, 20)], OrderStatus.new)
        self.assertEqual(order.getOrderAmount(), order_amount)

    def test_get_order_discount(self):
        cartUser = User('first_name', 'last_name', 'phone_number', 'address', 'email', 'password')
        productcart1 = ProductCart(Product(1, 'test1', 100), 1, 10)
        productcart2 = ProductCart(Product(2, 'test2', 200), 2, 20)
        order_discount = 30
        order = Order(cartUser, [productcart1, productcart2], OrderStatus.new)
        self.assertEqual(order.getOrderDicount(), order_discount)

    def test_get_delivery_address(self):
        cartUser = User('first_name', 'last_name', 'phone_number', 'Fesenko1', 'email', 'password')
        productcart1 = ProductCart(Product(1, 'test1', 100), 1, 10)
        productcart2 = ProductCart(Product(2, 'test2', 200), 2, 20)
        delivery_address = 'Fesenko1'
        order = Order(cartUser, [productcart1, productcart2], OrderStatus.new)
        self.assertEqual(order.getDeliveryAddress(), delivery_address)

    def test_get_delivery_status(self):
        cartUser = User('first_name', 'last_name', 'phone_number', 'address', 'email', 'password')
        productcart1 = ProductCart(Product(1, 'test1', 100), 1, 10)
        productcart2 = ProductCart(Product(2, 'test2', 200), 2, 20)
        delivery_status = 1
        order = Order(cartUser, [productcart1, productcart2], OrderStatus.new)
        self.assertEqual(order.getDeliveryStatus(), delivery_status)

    def test_get_order_user_data(self):
        cartUser = User('Den', 'Vasin', '0503616655', 'Fesenko1', 'den2001@ukr.net', 'password')
        productcart1 = ProductCart(Product(1, 'test1', 100), 1, 10)
        productcart2 = ProductCart(Product(2, 'test2', 200), 2, 20)
        order = Order(cartUser, [productcart1, productcart2], OrderStatus.new)
        user_data_list = ['Den Vasin', 'Fesenko1', '0503616655', 'den2001@ukr.net']
        self.assertEqual(order.getOrderUserData(), user_data_list)

    def test_get_order_products_data(self):
        cartUser = User ('Den', 'Vasin', '0503616655', 'Fesenko1', 'den2001@ukr.net', 'password')
        productcart1 = ProductCart (Product (1, 'test1', 100), 1, 10)
        productcart2 = ProductCart (Product (2, 'test2', 200), 2, 20)
        order = Order (cartUser, [productcart1, productcart2], OrderStatus.new)
        products_data_list = ['test1|100|1|10', 'test2|200|2|20']
        self.assertEqual (order.getOrderProductsData(), products_data_list)


unittest.main()