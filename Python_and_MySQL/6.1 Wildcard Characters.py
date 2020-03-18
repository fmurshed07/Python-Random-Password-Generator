'''
You can also select the records that starts,
includes, or ends with a given letter or phrase.

Use the %  to represent wildcard characters
Select records where the address contains the word "way"
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="test"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address LIKE '%Nagar%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for i in myresult:
    print(i)
