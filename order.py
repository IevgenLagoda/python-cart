import re
from enum import Enum, auto
from cart import Cart
from user import User
from product import Product
from productcart import ProductCart

class OrderStatus(Enum):
    new = auto()
    order_processing = auto()
    delivery = auto()
    received = auto()

    def __str__(self):
        return 'Order status: {0}'.format(self.value)

class Order:
    def __init__(self, user, products, order_status):
        self.cart = Cart(user)
        self.user = user
        self.order_status = order_status
        if len(products) == 0:
            return
        for product in products:
            if isinstance(product, ProductCart):
                self.cart.addProductToCart(product)
            elif isinstance(product, (tuple, list)):
                product, amount, discount = product
                self.cart.addProductToCart(product, amount, discount)

    def getOrderAmount(self):
        return self.cart.getTotalCartPrice()

    def getOrderDicount(self):
        return self.cart.getTotalDicount()

    def getDeliveryAddress(self):
        return self.user.getAddress()

    def getDeliveryStatus(self):
        return self.order_status.value

    # TODO: setNextDeliveryStatus(self)
    def setNextDeliveryStatus(self):
        match self.getDeliveryStatus():
            case OrderStatus.new.value:
                self.order_status = OrderStatus.order_processing
            case OrderStatus.order_processing.value:
                self.order_status = OrderStatus.delivery
            case OrderStatus.delivery.value:
                self.order_status = OrderStatus.received

    def getOrderUserData(self):
        return [self.user.getFullName(), self.getDeliveryAddress(),
                self.user.getPhoneNumber(), self.user.getEmail()]

    def getOrderProductsData(self):
       products_list = ['{}|{}|{}|{}'.format(product_values.getName(), product_values.getPrice(),
                                             product_values.getAmount(), product_values.getDiscount())
                        for product_values in self.cart.products.values()]
       return products_list

    def exportToFile(self, filename):
        file_write_list = self.getOrderUserData() + self.getOrderProductsData()
        file_write_list.append(str(self.getOrderAmount()))
        file_write_list.append(str(self.getOrderDicount()))
        self.writeListToFile(file_write_list, filename)

    def writeListToFile(self, write_list, filename):
        try:
            with open(filename, 'w') as filename:
                if isinstance(write_list, list):
                    for line in write_list:
                        filename.write('- {}\n'.format(line))
        except IOError:
            # TODO: raise IOError("Writing error")
            raise IOError("Writing file error")

    @staticmethod
    def createNewOrder(filename):
        user, products_list = Order.importFromFile(filename)
        return Order(user, products_list, OrderStatus.new)
    
    # TODO: can we avoid code duplication with getOrderFromFile?
    # TODO: importFromFile should fill the Order in place.
    def updateCurrentOrder(self, filename):
        user, products_list = Order.importFromFile(filename)
        if len(products_list) < 5:
            self.user = user
        self.user = user
        for product in products_list:
            if isinstance(product, ProductCart):
                self.cart.addProductToCart(product)
            elif isinstance(product, (tuple, list)):
                product, amount, discount = product
                self.cart.addProductToCart(product, amount, discount)

    @staticmethod
    def importFromFile(filename):
        import_list = Order.readDataFromFile(filename)
        if len(import_list) == 0:
            raise 'File empty'
        if re.findall(r'([A-Z][a-z]{2,})\s([A-Z][a-z]{2,})', import_list[0]):
            first_name, last_name = re.findall (r'[A-Z][a-z]{2,}', import_list[0])
        else:
            first_name, last_name = '', ''
        if re.findall(r'[A-Z][a-z]{2,}.+\d+', import_list[1]):
            address, = re.findall (r'[A-Z][a-z]{2,}.+\d+', import_list[1])
        else:
            address = ''
        if re.findall(r'(?<=\s)[+ -d]{10,17}\b', import_list[2]):
            phone, = re.findall (r'(?<=\s)[+ -d]{10,17}\b', import_list[2])
        else:
            phone = ''
        if re.findall(r'[A-z._]+[\d]*@[A-z-]+\.[A-z]+.[A-z]*', import_list[3]):
            email, = re.findall(r'[A-z._]+[\d]*@[A-z-]+\.[A-z]+.[A-z]*', import_list[3])
        else:
            email = ''
        user = User(first_name, last_name, phone, address, email, '')
        products_cart_list = []
        if len(import_list) < 5:
            return user, products_cart_list
        for str_number in range(4, len(import_list) - 2):
            product_data = import_list[str_number].strip('- \n')
            name, price, amount, discount = product_data.split('|')
            price, amount, discount = int(price), int(amount), int(discount)
            productcart = ProductCart(Product (str_number, name, price), amount, discount)
            products_cart_list.append(productcart)
        return user, products_cart_list

    @staticmethod
    def readDataFromFile (filename):
        try:
            with open(filename, 'r') as file:
                import_list = file.readlines()
            return import_list
        except(IOError):
            # TODO: raise IOError("Writing error")
            raise IOError("Reading file error")