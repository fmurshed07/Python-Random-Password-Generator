# Check if Table Exists
# You can check if a database exist by listing all tables in your database by using the "SHOW TABLES" statement:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)