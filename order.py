import enum
from cart import Cart
from user import User
from product import Product

class OrderStatus(enum.Enum):

    new = 'Заказ оформлен'
    order_processing = 'Отбратока заказ складом'
    delivery = 'Товар отправлен'

# TODO: class should be besed on the Cart or to have self.cart
class Order:
    def __init__(self, user, products, order_status):
        self.user = user
        self.products = products
        self.order_status = order_status

    def getOrderAmount(self):
        # TODO: we can't use cart from outside of the class.
        return cart.getTotalCartPrice()

    def getOrderDicount(self):
        # TODO: can we use something from Cart here?
        total_discount = 0
        for product_values in self.products.values():
            total_discount += float(product_values.getDiscount())
        return total_discount

    # TODO: should use direct method from User
    def getDeliveryAddress(self):
        return self.user.user.getAddress()

    # TODO: we have to store status as enum member but return only value
    def getDeliveryStatus(self):
        return self.order_status

    def getOrderUserData(self):
        # TODO: we cna't use order.getDeliveryAddress()
        return [self.user.user.getFullName(), order.getDeliveryAddress(),
                self.user.user.getPhoneNumber(), self.user.user.getEmail()]

    # TODO please check the name
    def getOrderProdutsData(self):
       products_list = ['{}|{}|{}|{}'.format(product_values.getName(), product_values.getPrice(),
                                             product_values.getAmount(), product_values.getDiscount())
                        for product_values in self.products.values()]
       return products_list

    # TODO: exprotToFile(self, filename) and can hanlde everything inside.
    def getWriteFileOrder(self, order):
        file_write_list = self.getOrderUserData() + self.getOrderProdutsData()
        file_write_list.append(str(self.getOrderAmount()))
        file_write_list.append(str(self.getOrderDicount()))
        for line in file_write_list:
            order.write('- {} \n'.format(line))


if __name__ == "__main__":
    cartUser = User("Den", "Vasin", "0503616655", "Fesenko 1", "den2001@ukr.net", "qwerty")
    product1 = Product(1, 'notebook HP', 400)
    product2 = Product(2, 'notebook Acer', 350)

    cart = Cart(cartUser)
    cart.addProductToCart(product1, 2, 10)
    cart.addProductToCart(product2, 4, 20)

    # TODO: 1st param shoyld be cartUser.
    order = Order(cart, cart.products, OrderStatus.new.value)
    print(order.getOrderAmount())
    print(order.getDeliveryAddress())
    print(OrderStatus.new.value)
    try:
        with open('order.txt', 'w') as results:
            order.getWriteFileOrder(results)
    except IOError:
        print('File problem')

