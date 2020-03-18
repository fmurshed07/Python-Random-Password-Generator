'''
When selecting records from a table,
you can filter the selection by using the "WHERE" statement

Select record(s) where the address is "Park Lane 38":
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
sql = (" SELECT * FROM customers WHERE address = 'Vasant Nagar' ")
mycursor.execute(sql)

myresult = mycursor.fetchall()

print(myresult)
