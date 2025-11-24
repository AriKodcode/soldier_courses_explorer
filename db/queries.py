def search_by_institution_name(conn,word):
    cn = conn
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


def search_by_course_name(conn,word):
    cn = conn
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


def search_the_5_most_common_course(conn):
    cn = conn
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


def search_the_institution_most_common_course(conn):
    cn = conn
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


def search_the_least_common_course(conn):
    cn = conn
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


def show_course_count_per_district(conn):
    cn = conn
    cursor = cn.cursor()
    cursor.execute(f"""
    SELECT district, COUNT(*) AS num_courses
    FROM courses
    GROUP BY district
    ORDER BY num_courses DESC;
    """)
    for row in cursor.fetchall():
        print(row)
    cursor.close()


def show_courses_for_specific_district(conn,district):
    cn = conn
    cursor = cn.cursor()
    cursor.execute(f"""
    SELECT institution, city, course, telephone, email
    FROM courses
    WHERE district = '{district}';
    """)
    for row in cursor.fetchall():
        print(row)
    cursor.close()


def run_free_query(conn):
    cn = conn
    cursor = cn.cursor()
    while True:
        sql = input("Enter your sql queries")
        if sql[0:6].lower() == 'select':
            try:
                cursor.execute(f"{sql}")
                for row in cursor.fetchall():
                    print(row)
                cursor.close()
            except Exception as err:
                print(err)
            break


