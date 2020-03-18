'''
Delete Record
You can delete records from an existing table by using the "DELETE FROM" statement

Delete any record where the address is "Mountain 21"


Notice the WHERE clause in the DELETE syntax:
The WHERE clause specifies which record(s) that should be deleted.
If you omit the WHERE clause, all records will be deleted!!!
'''


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Vasant Nagar'"

mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, 'record(s) deleted')