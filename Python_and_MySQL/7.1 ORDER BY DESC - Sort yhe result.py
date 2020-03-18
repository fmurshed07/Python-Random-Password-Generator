'''
ORDER BY DESC
Use the DESC keyword to sort the result in a descending order.

Sort the result reverse alphabetically by name
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for i in myresult:
    print(i)