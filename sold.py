# Sold Items 
# Modified from code by Corey M Schafer
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-SQLite/employee.py

class Sold:

    def __init__(self, item_name, price, quantity, seller, buyer):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.seller = seller
        self.buyer = buyer

    def __repr__(self):
        return "Sold('{}', {}, {}, '{}', '{}')".format(self.item_name, self.price, self.quantity, self.seller, self.buyer)
