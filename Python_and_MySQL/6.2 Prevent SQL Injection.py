'''
Prevent SQL Injection
When query values are provided by the User, you should escape the values.

This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
The mysql.connector module has methods to escape query values

Escape query values by using the placholder %s method:
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("KPHB Phase 6",)

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for i in myresult:
    print(i)

