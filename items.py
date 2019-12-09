# Item information
# Modified from code by Corey M Schafer
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-SQLite/employee.py

class Items:

    def __init__(self, item_name, price, stock, seller):
        self.item_name = item_name
        self.price = price
        self.stock = stock
        self.seller = seller

    def __repr__(self):
        return "Seller('{}', {}, {}, '{}')".format(self.item_name, self.price, self.stock, self.seller)
