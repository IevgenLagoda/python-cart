from enum import Enum, auto
from cart import Cart
from user import User
from product import Product
from productcart import ProductCart

class OrderStatus(Enum):
    new = auto()
    order_processing = auto()
    delivery = auto()

    def __str__(self):
        return 'Order status: {0}'.format(self.value)

class Order:
    def __init__(self, user, products, order_status):
        self.cart = Cart(user)
        if len(products) == 0:
            return
        for product in products:
            if isinstance(product, ProductCart):
                self.cart.addProductToCart(product)
            elif isinstance(product, (tuple, list)):
                product, amount, discount = product
                self.cart.addProductToCart(product, amount, discount)
        self.order_status = order_status
        self.user = user

    def getOrderAmount(self):
        return self.cart.getTotalCartPrice()

    def getOrderDicount(self):
        return self.cart.getTotalDicount()

    def getDeliveryAddress(self):
        return self.user.getAddress()

    def getDeliveryStatus(self):
        return self.order_status.value

    def getOrderUserData(self):
        return [self.user.getFullName(), self.getDeliveryAddress(),
                self.user.getPhoneNumber(), self.user.getEmail()]

    def getOrderProductsData(self):
       products_list = ['{}|{}|{}|{}'.format(product_values.getName(), product_values.getPrice(),
                                             product_values.getAmount(), product_values.getDiscount())
                        for product_values in self.cart.products.values()]
       return products_list

    def exportToFile(self, filename):
        file_write_list = self.getOrderUserData() + self.getOrderProductsData()
        file_write_list.append(str(self.getOrderAmount()))
        file_write_list.append(str(self.getOrderDicount()))
        self.writeListToFile(file_write_list, filename)

    def writeListToFile(self, write_list, filename):
        try:
            with open(filename, 'w') as filename:
                if isinstance(write_list, list):
                    for line in write_list:
                        filename.write('- {} \n'.format(line))
        except IOError:
            return 'File problem'

# TODO: remove when moved to test.