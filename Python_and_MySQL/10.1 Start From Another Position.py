'''
Start From Another Position

If you want to return five records, starting from the 3 (third) record,
you can use the "OFFSET" keyword

Start from position 3, and return 5 records
'''

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)