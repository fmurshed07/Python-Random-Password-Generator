'''
It is considered a good practice to escape the values of any query, also in delete statements.

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

sql = 'DROP TABLE customers'
mycursor.execute(sql)