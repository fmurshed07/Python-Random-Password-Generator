'''
To fill a table in MySQL, use the "INSERT INTO" statement.

Important!: Notice the statement: mydb.commit().
It is required to make the changes, otherwise no changes are made to the table.
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
val = ('Sitaram', 'KPHB Phase 6')

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, 'record inserted')