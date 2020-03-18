import mysql.connector
# Creating a Table
# To create a table in MySQL, use the "CREATE TABLE" statement.
# Make sure you define the name of the database when you create the connection

mydb = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='admin',
    database='test'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")