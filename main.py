import mysql.connector

# connection details to replace
myDB = mysql.connector.connect(
     host = "localhost"
     user = "root"
     password = "password"
     database = "CrystaltestDB"
)

# create a cursor object
mycursor = myDB.cursor

# simple sql query
sql = "SELECT * FROM users"

# execute query with command
mycursor.execute(sql)

# fetch results
myresults = mycursor.fetchall()
