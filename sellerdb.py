import sqlite3
from seller import Seller

conn = sqlite3.connect('seller.db')

c = conn.cursor()

c.execute("""CREATE TABLE Sellers ( 
            username text
            )""")
 
