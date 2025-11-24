from db.queries import *
from db.load_csv import load_csv
import db.connection

def db_app():
    print("DATA BASE")
    conn = db.connection.make_connection()
    while True:
        choose = 0
        while not 0 < choose < 11:
            print("""
            MENU:\n
            Choose a number between 1 and 10\n
            1. for search by institution name\n
            2. for search by course name\n
            3. for search the 5 most common course\n
            4. for search the institution most common course\n
            5. for search the least common course\n
            6. for show course count per district\n
            7. for show courses for specific district\n
            8. for run free query\n
            9. to load csv\n
            10. for Exit
            """)
            choose = int(input())
        if choose == 1:
            word = input("enter your word")
            search_by_institution_name(conn,word)
        if choose == 2:
            word = input("enter your word")
            search_by_course_name(conn,word)
        if choose == 3:
            search_the_5_most_common_course(conn)
        if choose == 4:
            search_the_institution_most_common_course(conn)
        if choose == 5:
            search_the_least_common_course(conn)
        if choose == 6:
            show_course_count_per_district(conn)
        if choose == 7:
            district = input("enter your district")
            show_courses_for_specific_district(conn,district)
        if choose == 8:
            run_free_query(conn)
        if choose == 9:
            load_csv(conn)
        if choose == 10:
            print("Exit")
            break
        else:
            print("Press num between 1 and 10")
