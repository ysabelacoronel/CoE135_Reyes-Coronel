# Buyer information
# Modified from code by Corey M Schafer
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-SQLite/employee.py

class Buyer:

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "Buyer('{}')".format(self.username)
