import sqlite3

con = sqlite3.connect('books.db')

cursor = con.cursor()
sql_query = "CREATE TABLE Book (id integer PRIMARY KEY AUTO INCREMENT,author text NOT NULL,language text NOT NULL,title TEXT NOT NULL)"

cursor.execute(sql_query)
con.close()
