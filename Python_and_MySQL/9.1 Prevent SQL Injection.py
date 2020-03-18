'''
Prevent SQL Injection
It is considered a good practice to escape the values of any query, also in update statements.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

The mysql.connector module uses the placeholder %s to escape values in the delete statement:
'''

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="test"
)

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ('Bengaluru', 'Banglore')

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")