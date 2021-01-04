'''2.WAP to insert a new row in a database'''
import mysql.connector as con
Student=con.connect(
    host="localhost",
    user="root",
    password="bansari@123",
    database="lioncat"
)
cursor=Student.cursor()
command="INSERT INTO Students (Name,Age,City) VALUES (%s,%s,%s)"
val=("Lioncat",18,"London")
cursor.execute(command,val)

Student.commit()
print(cursor.rowcount,"record(s) inserted")
