import sqlite3
from buyer import Buyer

conn = sqlite3.connect('buyer.db')

c = conn.cursor()

c.execute("""CREATE TABLE Buyers ( 
            username text
            )""")
 
