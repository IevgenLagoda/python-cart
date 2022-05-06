from enum import Enum, auto
from cart import Cart
from user import User
from product import Product

class OrderStatus(Enum):
    new = auto
    order_processing = auto
    delivery = auto

class Order:
    def __init__(self, user, products, order_status):
        self.cart = Cart(user)
        # TBD: discuss overload.
        for product, amount, discount in products:
            self.cart.addProductToCart(product, amount, discount)
        self.order_status = order_status
        # TODO: remove the next line.

    def getOrderAmount(self):
        # TODO: we can't use cart from outside of the class.
        return self.cart.getTotalCartPrice()

    def getOrderDicount(self):
        # TODO: can we use something from Cart here?
        return self.cart.getTotalDicount()

    # TODO: should use direct method from User (not from cart)
    def getDeliveryAddress(self):
        return self.cart.user.getAddress()

    # TODO: we have to store status as enum member but return only value
    def getDeliveryStatus(self):
        return self.order_status

    def getOrderUserData(self):
        # TODO: we cna't use order.getDeliveryAddress()
        return [self.cart.user.getFullName(), order.getDeliveryAddress(),
                self.cart.user.getPhoneNumber(), self.cart.user.getEmail()]

    # TODO please check the name
    def getOrderProdutsData(self):
       products_list = ['{}|{}|{}|{}'.format(product_values.getName(), product_values.getPrice(),
                                             product_values.getAmount(), product_values.getDiscount())
                        for product_values in self.cart.products.values()]
       return products_list

    def importFile(self):
        try:
            with open('order.txt', 'w') as file_object:
                order.exportToFile(file_object)
        except IOError:
            return 'File problem'

    # TODO: exprotToFile(self, filename) and can hanlde everything inside.
    def exportToFile(self, file_object):
        file_write_list = order.getOrderUserData() + order.getOrderProdutsData()
        file_write_list.append(str(order.getOrderAmount()))
        file_write_list.append(str(order.getOrderDicount()))
        for line in file_write_list:
            file_object.write('- {} \n'.format(line))

if __name__ == "__main__":
    cartUser = User("Den", "Vasin", "0503616655", "Fesenko 1", "den2001@ukr.net", "qwerty")
    product1 = Product(1, 'notebook HP', 400)
    product2 = Product(2, 'notebook Acer', 350)

    # TODO: 3red param should be OrderStatus memeber, not a vlaue.
    order = Order(cartUser, [(product1, 2, 10), (product2, 4, 20)], OrderStatus.new)
    print(order.getOrderAmount())
    print(order.getDeliveryAddress())
    print(order.getDeliveryStatus())

