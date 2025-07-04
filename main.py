import mysql.connector as sqlconn

mysqlstry = ""

# connection details to replace
myDB = sqlconn.connect (
     host = "localhost",
     user = "appuser",
     password = "password",
     database = "CrystalsPracticeDB"
)

if myDB.is_connected():
    print("Successfully Connected to MySQL database.")
else:
    print("Check yo inputs, they really correct?")


# create a cursor object
mycursor = myDB.cursor

# simple sql query
sql = "SELECT * FROM students where student_id = " + mysqlstry


sql
# execute query with command
#results = mycursor.execute(sql)

# fetch results
# myresults = mycursor.fetchall()
