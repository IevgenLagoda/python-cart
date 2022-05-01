import enum
from cart import Cart
from user import User
from product import Product
from productcart import ProductCart

class OrderStatus(enum.Enum):

    new = 'Заказ оформлен'
    order_processing = 'Отбратока заказ складом'
    delivery = 'Товар отправлен'

class Order:
    def __init__(self, user, products, order_status):
        self.user = user
        self.products = products
        self.order_status = order_status

    def getOrderAmount(self):
        return cart.getTotalCartPrice()

    def getDeliveryAddress(self):
        return self.user.user.getAddress()


if __name__ == "__main__":
    cartUser = User("Den", "Vasin", "0503616655", "Fesenko 1", "den2001@ukr.net", "qwerty")
    product1 = Product(1, 'notebook HP', 400)
    product2 = Product(2, 'notebook Acer', 350)

    cart = Cart(cartUser)
    cart.addProductToCart(product1, 0, 10)
    cart.addProductToCart(product2, 4, 20)

    order = Order(cart, cart.products, OrderStatus.new.value)
    print(OrderStatus.new.value)
    print(order.getOrderAmount())
    print(order.getDeliveryAddress())
