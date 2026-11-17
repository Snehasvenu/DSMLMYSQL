import pymysql

connection = pymysql.connect(
    host='localhost',
    user='python_apps',
    password='Python@123',
    database='camerin_students_1',
    port=3306
)

def get_data():
     query="""
            SELECT * FROM students
            WHERE student_id = 102
        """
     cursor.execute(query)
     return cursor.fetchone()


try:
    with connection.cursor() as cursor:
       
        print("== original data ==")
        print(get_data())
        

        cursor.execute("""
             UPDATE students SET city=%s
             WHERE student_id=%s
             """, ('Delhi', 102))
        print("==After update(Before commit) ==")
        print(get_data())

        connection.commit()


        print("==After commit) ==")
        print(get_data())
        cursor.execute("""
             UPDATE students SET city=%s
             WHERE student_id=%s
             """, ('Thrissur', 102))


        print("==After Second update(Before rollback) ==") 
        print(get_data())


        connection.rollback()
        print("==After rollback) ==")
        print(get_data())


except Exception as e:
    print(f")  Error occured: {e}")

finally:
    connection.close()
    print("operations completed")     
        
 #newline(after adding in git ,if we type any code it will show modified in git status)