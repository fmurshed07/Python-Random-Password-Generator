'''
Limit the Result

You can limit the number of records returned from the query, by using the "LIMIT" statement.
Select the 5 first records in the "customers" table
'''

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="test"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)