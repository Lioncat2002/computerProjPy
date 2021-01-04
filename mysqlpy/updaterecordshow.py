'''3.WAP to Update a record in a table'''
import mysql.connector as con
Student=con.connect(
    host="localhost",
    user="root",
    password="bansari@123",
    database="lioncat"
)
cursor=Student.cursor()
command="UPDATE Students SET Age = 17 WHERE Age = 16"
cursor.execute(command)
Student.commit()
print(cursor.rowcount,"record(s) affected")