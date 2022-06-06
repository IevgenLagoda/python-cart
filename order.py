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
        if len(products) == 0:
            return
        for product in products:
            if isinstance(product, ProductCart):
                self.cart.addProductToCart(product)
            elif isinstance(product, (tuple, list)):
                product, amount, discount = product
                self.cart.addProductToCart(product, amount, discount)
        self.order_status = order_status
        self.user = user

    def getOrderAmount(self):
        return self.cart.getTotalCartPrice()

    def getOrderDicount(self):
        return self.cart.getTotalDicount()

    def getDeliveryAddress(self):
        return self.user.getAddress()

    def getDeliveryStatus(self):
        return self.order_status.value

    # TODO: setNextStatus(self)
    def setDeliveryStatus(self):
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
                        filename.write('- {} \n'.format(line))
        except IOError:
            raise IOError

    # TODO: filename should be a paramater.
    # TODO: if you return Order then name should be getOrderFromFile()
    # TODO: getOrderFromFile should be static.https://www.journaldev.com/18722/python-static-method#:~:text=What%20is%20a%20static%20method,an%20object%20for%20that%20class.
    # TODO: importFromFile should fill the Order in place.
    def importFromFile(self):
        try:
            with open('import.txt', 'r') as file:
                import_list = file.readlines ()
                if len(import_list) == 0:
                    raise 'File empty'
                # TODO: check if we have less than 5 lines
                # TODO: else? set the empty values ('')
                if re.findall(r'([A-Z][a-z]{2,})\s([A-Z][a-z]{2,})', import_list[0]):
                    first_name, last_name = re.findall(r'[A-Z][a-z]{2,}', import_list[0])
                # TODO: should accept addresses like:
                # TODO: 'Bandery 15, kv 4', 'Heroiv 12/2', 'Zelenskogo 4'
                if re.findall(r'[A-Z][a-z]{2,}\d+', import_list[1]):
                    address, = re.findall (r'[A-Z][a-z]{2,}\d+', import_list[1])
                # TODO: should accept more formats:
                # TODO: '+19492471682', '7-12-15', '+380667674093', '7421524'
                if re.findall(r'(?<=\s)[+ -d]{10,17}\b', import_list[2]):
                    phone, = re.findall(r'(?<=\s)[+ -d]{10,17}\b', import_list[2])
                # TODO: should accept more formats:
                # TODO: 'i@ua.fm', 'me.address.here@site.mobi', 'dory_mory@molly-dolly.co.uk'
                if re.findall(r'[A-z0-9._]+@[A-z]+\.[A-z]+.[A-z]+', import_list[3]):
                    email, = re.findall(r'[A-z0-9._]+@[A-z]+\.[A-z]+.[A-z]+', import_list[3])
                user = User(first_name, last_name, phone, address, email, '')
                # TODO: we should allow order w\o products.
                if len(import_list) < 5:
                    raise 'products not found'
                products_cart_list = []
                product_id = 0
                # TODO: file has the same format as generated by export.
                for str_number in range (4, len (import_list)):
                    if re.findall(r'\b[A-z0-9\s.-]+\b', import_list[str_number]):
                        product_id += 1
                        # TODO: it's better just to split by separator.
                        name, price, amount, discount = re.findall(r'\b[A-z0-9\s.-]+\b', import_list[str_number])
                        productcart = ProductCart(Product(product_id, name, price), amount, discount)
                        products_cart_list.append(productcart)
                return Order(user, products_cart_list, OrderStatus.new)  # or return user,  products_cart_list
        except(IOError):
            raise IOError