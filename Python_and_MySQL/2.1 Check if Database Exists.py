import mysql.connector
# You can check if a database exist
# by listing all databases in your system by using the "SHOW DATABASES" statement:

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin"
)

mycursor = mydb.cursor()
mycursor.execute('SHOW DATABASES')

for db in mycursor:
    print(db)



# Or you can try to access the database when making the connection:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="abcd",

  database="mydatabase"
)