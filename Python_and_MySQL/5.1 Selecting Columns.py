'''
To select only some of the columns in a table, use the "SELECT" statement
followed by the column name(s)

Select only the name and address columns:
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
mycursor.execute('SELECT name, address FROM customers')

myresult = mycursor.fetchall()
for i in myresult:
    print(i)