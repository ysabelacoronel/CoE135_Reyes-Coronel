import sqlite3
from items import Items

conn = sqlite3.connect('items.db')

c = conn.cursor()

c.execute("""CREATE TABLE items (
           item_name text,
            price integer,
            stock integer,
            seller text
            )""")
 
