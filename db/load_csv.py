import csv
from db.connection import make_connection


def load_csv():
    cnx = make_connection()
    cursor = cnx.cursor()

    with open("C:/Users/internet/Desktop/soldier_courses_explorer/data/courses.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            cursor.execute("""
                INSERT INTO courses 
                (institution, city, address, course,
                district, telephone, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """, row)

    cnx.commit()
    cursor.close()
    cnx.close()



