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


def search_the_5_most_common_course():
    cn = db.connection.make_connection()
    cursor = cn.cursor()
    cursor.execute(f"""
        SELECT course, COUNT(*) AS num
        FROM courses
        GROUP BY course
        ORDER BY num DESC
        LIMIT 5;
        """)
    print("top 5 common course\n")
    for row in cursor.fetchall():
        print(row)
    cursor.close()


def search_the_institution_most_common_course():
    cn = db.connection.make_connection()
    cursor = cn.cursor()
    cursor.execute(f"""
        SELECT institution
        FROM courses
        WHERE course = (
        SELECT course
        FROM courses
        GROUP BY course
        ORDER BY COUNT(*) DESC
        LIMIT 1);
        """)
    print("the institution of the most courses\n")
    for row in cursor.fetchall():
        print(row)
    cursor.close()


search_the_5_most_common_course()
search_the_institution_most_common_course()


def search_the_least_common_course():
    cn = db.connection.make_connection()
    cursor = cn.cursor()
    cursor.execute(f"""
    SELECT course, COUNT(*) AS num
    FROM courses
    GROUP BY course
    ORDER BY num ASC
    LIMIT 1;
    """)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
