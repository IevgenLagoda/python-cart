from product import Product
from user import User
from cartproduct import ProductCart # переименование класса
from userloginpassword import UserLoginPassword

class Cart:
    def __init__(self, user, loginpassword):
        self.user = user
        self.loginpassword = loginpassword
        self.products = {}

    def addProductToCart(self, product, amount=1, discount=0):
        id = product.getId()
        if id not in self.products:
            self.products[id] = ProductCart(product, amount, discount)
        else:
            self.products[id].setAmount(self.products[id].getAmount + amount)
        self.products[id].setDiscount(discount)

    def isUserValid(self):
        return self.user.isFullNameExists() and self.user.isAddressExists() and self.user.isPhoneNumberExists()

    def UserAuth(self, login, password):
        return self.loginpassword.getLogin() == login and self.loginpassword.getPassword() == password  # переименование метода, замена if на return, изменения местарасположения кода метода в классе

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
        if amount == 0 or amount >= self.products[id].getAmount():
            del self.products[id]
        else:
            self.products[id].setAmount(self.products[id].getAmount() - amount)
        return self.products[id].getAmount()


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
    print(cart.UserAuth('den2001@ukr.net', 'password'))