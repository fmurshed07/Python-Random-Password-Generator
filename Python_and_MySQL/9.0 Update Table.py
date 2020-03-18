'''
Update Table
You can update existing records in a table by using the "UPDATE" statement

Overwrite the address column from "Valley 345" to "Canyoun 123"

Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or records that should be updated.
If you omit the WHERE clause, all records will be updated!
'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="test"
)

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Chennai' WHERE address = 'Madras'"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")