import mysql.connector

# Creating a Database
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin"
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE test')