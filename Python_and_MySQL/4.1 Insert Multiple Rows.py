'''
To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples,
containing the data you want to insert
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
sql = "INSERT INTO products (name, fav) VALUES (%s, %s)"
val = [
  ('Sitaram', '154'),
  ('Ali', '154'),
  ('John', '155'),
  ('Harish', ''),
  ('Michael',''),

]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, 'was inserted')

