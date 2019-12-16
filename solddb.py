import sqlite3
from sold import SoldItems

conn = sqlite3.connect('sold.db')

c = conn.cursor()

c.execute("""CREATE TABLE SoldItems (
           item_name text,
            price integer,
            quantity integer,
            seller text
            buyer text
            )""")
 
