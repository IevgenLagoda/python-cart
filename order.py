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
        return [self.user.getFullName(), order.getDeliveryAddress(),
                self.user.getPhoneNumber(), self.user.getEmail()]

    def getOrderProductsData(self):
       products_list = ['{}|{}|{}|{}'.format(product_values.getName(), product_values.getPrice(),
                                             product_values.getAmount(), product_values.getDiscount())
                        for product_values in self.cart.products.values()]
       return products_list

    def exportToFile(self, filename):
        file_write_list = order.getOrderUserData() + order.getOrderProductsData()
        file_write_list.append(str(order.getOrderAmount()))
        file_write_list.append(str(order.getOrderDicount()))
        order.writeListToFile(file_write_list, filename)

    def writeListToFile(self, write_list, filename):
        try:
            with open(filename, 'w') as filename:
                if isinstance(write_list, list):
                    for line in write_list:
                        filename.write('- {} \n'.format(line))
        except IOError:
            return 'File problem'

if __name__ == "__main__":
    cartUser = User("Den", "Vasin", "0503616655", "Fesenko 1", "den2001@ukr.net", "qwerty")
    product1 = Product(1, 'notebook HP', 400)
    product2 = Product(2, 'notebook Acer', 350)
    productcart1 = ProductCart(product1, 2, 10)

    order = Order(cartUser, [productcart1, (product2, 4, 20)], OrderStatus.new)
    print(order.getOrderAmount())
    print(order.getDeliveryAddress())
    print(order.getDeliveryStatus())
    order.exportToFile('order.txt')
