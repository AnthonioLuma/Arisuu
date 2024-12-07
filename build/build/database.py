import sqlite3


#define connection and cursor
connection = sqlite3.connect("store_arisu.db")

cursor = connection.cursor()

cashier= """CREATE TABLE IF NOT EXISTS
cashier(product_name TEXT NOT NULL,
product_quantity INTEGER,
product_price FLOAT)"""

cursor.execute(cashier)

inventory= """CREATE TABLE IF NOT EXISTS
cashier(product_name2 TEXT NOT NULL,
product_quantity INTEGER,
remaining_stock INTEGER)"""

cursor.execute(inventory)

