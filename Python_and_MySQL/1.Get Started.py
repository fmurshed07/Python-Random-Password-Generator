import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin"
)

print("Connecting to database ....")
print(mydb)