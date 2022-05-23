from product import Product
from user import User
from productcart import ProductCart  # переименование класса

class Cart:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def addProductToCart(self, product, amount=1, discount=0):
        if isinstance(product, ProductCart):
            if product.getAmount() == 0:
                return
            id = product.getId()
            if id not in self.products:
                self.products[id] = product
            else:
                self.products[id].setAmount(self.products[id].getAmount() + product.getAmount())
            self.products[id].setDiscount(product.getDiscount())
        elif isinstance(product, Product):
            if amount == 0:
                return
            id = product.getId()
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