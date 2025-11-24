import mysql.connector
from config import db_config

def make_connection():
    dict1 = db_config()
    cnx = mysql.connector.connect(
        host=dict1["host"],
        user=dict1["user"],
        password=dict1["password"],
        database=dict1["database"]
    )
    return cnx