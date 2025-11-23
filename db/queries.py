import db.connection

def search_by_institution_name(word):
    cn = db.connection.make_connection()
    cursor = cn.cursor()
    cursor.execute(f"""
    SELECT id, institution, city, course, district, telephone, email
    FROM courses
    WHERE institution LIKE CONCAT('%{word}%')
    LIMIT 50;
    """)
    for row in cursor.fetchall():
        print(row)
    cursor.close()

def search_by_course_name(word):
    cn = db.connection.make_connection()
    cursor = cn.cursor()
    cursor.execute(f"""
        SELECT id, institution, city, course, district, telephone, email
        FROM courses
        WHERE course LIKE CONCAT('%{word}%')
        LIMIT 50;
        """)
    for row in cursor.fetchall():
        print(row)
    cursor.close()




