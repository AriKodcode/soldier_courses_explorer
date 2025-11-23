import mysql.connector

def make_connection():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="soldier_courses_db"
    )
    return cnx