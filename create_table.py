import sqlite3

connection=sqlite3.connect("data.db")
cursor=connection.cursor()

create_table="Create Table IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table)

#Table item

create_table="Create Table IF NOT EXISTS items (name text,price real)"
cursor.execute(create_table)

connection.commit()
connection.close()
