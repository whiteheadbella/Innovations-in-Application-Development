import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursorObj = database.cursor()

cursorObj.execute("CREATE DATABASE EmployeeSystem")

print("Database created successfully")