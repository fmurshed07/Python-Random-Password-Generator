'''
To select from a table in MySQL, use the "SELECT" statement

Select all records from the "customers" table, and display the result

Note: We use the fetchall() method,
which fetches all rows from the last executed statement.
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM customers')
myresult = mycursor.fetchall()

print(myresult)

for item in myresult:
    print(item)