import mysql.connector import pymysql try: conn = mysql.connector.connect(
    host = "localhost",
    user = "crystalchanell",
    password = "password",
    database = "CrystaltestDB" cursor = conn.cursor() cursor.execute("SELECT * FROM your_table") results = cursor.fetchall() cursor.close()
) if conn.is_connected(): print("connected to database")
else: print("failed to connect to database")
except mysql.connector.Error as err: print(f "Error: (err)") finally: if conn.is_connected(): conn.close() print("connection is closed")