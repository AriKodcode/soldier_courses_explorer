import csv

import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="classicmodels"
)
print("connected, server version:", cnx.get_server_info())
cursor = cnx.cursor()
cursor.execute("select * from offices")
data = cursor.fetchall()
for i in data:
    print(i)

