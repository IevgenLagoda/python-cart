from product import Product

class CartProduct(Product):

    def __init__(self, product, amount, discount):
        self.amount = amount
        self.discount = discount
        self.product = product

    def getProduct(self):
        return self.product

    def getAmount(self):
        return self.amount

    def getDiscount(self):
        return self.discount

    def setAmount(self, amount):
        self.amount = amount

    def setDiscount(self, discount):
        self.discount = discount

    def getProductTotalPrice(self):
        return self.product.getPrice() * self.amount - self.discount









