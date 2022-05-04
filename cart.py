from product import Product
from user import User
from productcart import ProductCart  # переименование класса

class Cart:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def addProductToCart(self, product, amount=1, discount=0):
        # TODO: check if amount == 0 and return nothing.
        id = product.getId()
        if amount == 0:
            return
        if id not in self.products:
            self.products[id] = ProductCart(product, amount, discount)
        else:
            self.products[id].setAmount(self.products[id].getAmount() + amount)
        self.products[id].setDiscount(discount)

    def isUserValid(self):
        return self.user.isUserDataExists()

    def isUserAuthValid(self, login, password):
        return self.user.canBeLogged(login, password)

    def getTotalCartPrice(self):
        total = 0
        if self.isCartEmpty():
            return total
        for id in self.products:
            total += self.products[id].getProductTotalPrice()
        return total

    def isCartEmpty(self):
        return len(self.products) == 0

    def getProductById(self, id):
        if self.isCartEmpty():
            return None
        return self.products[id].getProduct()

    def removeProductById(self, id, amount=0):
        if self.isCartEmpty():
            raise 'Cart is Empty'  # вызов исключение если корзина пуста
        if amount >= self.products[id].getAmount():
            del self.products[id]
        else:
            self.products[id].setAmount(self.products[id].getAmount() - amount)
        return self.products[id].getAmount()

if __name__ == "__main__":
    cartUser = User("Den", "Vasin", "0503616655", "Fesenko 1", "den2001@ukr.net", "qwerty")
    product1 = Product(1, 'notebook HP', 400)
    product2 = Product(2, 'notebook Acer', 350)

    cart = Cart(cartUser)
    cart.addProductToCart(product1, 0, 10)
    cart.addProductToCart(product2, 4, 20)

    print(cart.getTotalCartPrice())
    print(cart.removeProductById(2, 2))
    print(cart.isUserValid())
    print(cart.isUserAuthValid("den2001@ukr.net", "qwerty"))
