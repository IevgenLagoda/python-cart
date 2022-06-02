import re

def importFromFile():
    try:
        with open('import.txt', 'r') as file:
            import_list = file.readlines()
            if len(import_list) == 0:
                raise 'File empty'
            if re.findall(r'([A-Z][a-z]{2,})\s([A-Z][a-z]{2,})', import_list[0]):
                first_name, last_name = re.findall(r'[A-Z][a-z]{2,}', import_list[0])
            if re.findall(r'[A-Z][a-z]{2,}\d+', import_list[1]):
                address, = re.findall(r'[A-Z][a-z]{2,}\d+', import_list[1])
            if re.findall(r'(?<=\s)[+ -d]{10,17}\b', import_list[2]):
                phone, =  re.findall(r'(?<=\s)[+ -d]{10,17}\b', import_list[2])
            if re.findall(r'[A-z0-9._]+@[A-z]+\.[A-z]+.[A-z]+', import_list[3]):
                email, = re.findall(r'[A-z0-9._]+@[A-z]+\.[A-z]+.[A-z]+', import_list[3])
            if len(import_list) < 5:
                raise 'products no found'
            productcart_list = []
            product_id = 0
            for str_number in range(4, len(import_list)):
                if re.findall(r'\b[A-z0-9\s.-]+\b', import_list[str_number]):
                    product_id += 1
                    name, price, amount, discount = re.findall(r'\b[A-z0-9\s.-]+\b', import_list[str_number])
                    print(product_id, name, price, amount, discount)
                    productcart_list.append([name, price, amount,discount])
        return first_name, last_name, address, phone, email, productcart_list
    except(IOError):
        raise IOError


print(importFromFile())
