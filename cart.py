from product import Product
from user import User
from cartproduct import CartProduct
from userloginpassword import UserLoginPassword

class Cart:
    def __init__(self, user, loginpassword):
        self.user = user
        self.loginpassword = loginpassword
        self.products = {}

    def addProductToCart(self, product, amount=1, discount=0):   # Use to check product
        id = product.getId()
        if id not in self.products:
            self.products[id] = CartProduct(product, amount, discount)
        else:
            self.products[id].setAmount(self.products[id].getAmount + amount)
        self.products[id].setDiscount(discount)

    def isUserValid(self):
        return self.user.isFullNameExists() and self.user.isAddressExists() and self.user.isPhoneNumberExists()

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
            return None
        if amount == 0 or amount >= self.products[id].getAmount():
            del self.products[id]
        else:
            self.products[id].setAmount(self.products[id].getAmount() - amount)
        return self.products[id].getAmount()

    def canBeLogged(self, login, password):
        if self.loginpassword.getLogin() == login and self.loginpassword.getPassword() == password:
            return True
        return False


if __name__ == "__main__":
    cartUser = User("Den", "Vasin", "", "")
    product1 = Product(1, 'notebook HP', 400)
    product2 = Product(2, 'notebook Acer', 350)
    loginpassword = UserLoginPassword('den2001@ukr.net', 'qwerty')

    cart = Cart(cartUser, loginpassword)
    cart.addProductToCart(product1, 1, 10)
    cart.addProductToCart(product2, 4, 20)

    print(cart.getTotalCartPrice())
    print(cart.removeProductById(2, 2))
    print(cart.canBeLogged('den2001@ukr.net', 'password'))