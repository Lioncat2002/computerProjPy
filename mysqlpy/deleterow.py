'''4.WAP to delete a row from a table in mysql table'''
import mysql.connector as con
Student=con.connect(
    host="localhost",
    user="root",
    password="bansari@123",
    database="lioncat"
)
cursor=Student.cursor()
command="DELETE FROM Students WHERE Age=17"
cursor.execute(command)

Student.commit()
print(cursor.rowcount,"record(s) deleted")