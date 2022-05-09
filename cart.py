from product import Product
from user import User
from productcart import ProductCart  # переименование класса


class Cart:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def addProductToCart(self, product, amount=1, discount=0):
        # TODO: to check the instance of `product`. We can use `isinstance`.
        # TODO: we have to support `Product` and `ProductCart` typex.
        id = product.getId()
        if amount == 0:
            return
        if id not in self.products:
            if isinstance(product, Product):
                self.products[id] = ProductCart(product, amount, discount)
            elif isinstance(product, ProductCart):
                self.products[id] = (product, amount, discount)
        else:
            self.products[id].setAmount(self.products[id].getAmount() + amount)
        self.products[id].setDiscount(discount)
        print(self.products)

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

    def getTotalDicount(self):
        total_discount = 0
        for product_values in self.products.values():
            total_discount += float(product_values.getDiscount())
        return total_discount

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
    productCart1 = ProductCart(product1, 1, 10)
    productCart2 = ProductCart(product2, 2, 20)
    cart.addProductToCart(product1, 0, 10)
    cart.addProductToCart(product2, 4, 20)

    print(cart.getTotalCartPrice())
    print(cart.removeProductById(2, 2))
    print(cart.isUserValid())
    print(cart.isUserAuthValid("den2001@ukr.net", "qwerty"))
    print(cart.getTotalDicount())
