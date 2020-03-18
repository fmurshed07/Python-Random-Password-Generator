'''
You can get the id of the row you just inserted by asking the cursor object.

Note: If you insert more that one row, the id of the last inserted row is returned.
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
val = ('Tambi', 'Madras')

mycursor.execute(sql, val)
mydb.commit()

print('1 record inserted, ID: ', mycursor.lastrowid)
