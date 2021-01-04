'''1.WAP in python to display the contents of a mysql table'''
import mysql.connector as con

Student=con.connect(
    host="localhost",
    user="root",
    password="bansari@123",
    database="lioncat"
)
cursor=Student.cursor()

cursor.execute("SELECT * FROM Students")
res=cursor.fetchall()
for x in res:
    print(x)