import pymysql

connection = pymysql.connect(
    host='localhost',
    user='python_apps',
    password='Python@123',
    database='camerin_students_1',
    port=3306
)

print("MYSQL connection is successful")

try:
    #cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        #records=cursor.fetchall()
        #records=cursor.fetchone()
        #records=cursor.fetchmany(3)
        #print (records)

        query = f"""SELECT * FROM students WHERE city = 'kochi'"""
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

        #for record in records:
            #print(record)


     #user_input=" OR '1'='1"
     #query = f"""SELECT * FROM users WHERE s_name = '{user_input}' """
     #cursor.execute(query)
     #print(cursor.fetchall())



    # INSERT OPERATION
    query= """
           INSERT INTO students VALUES (%s, %s, %s,%s)
           """
    values = (106, 'akhil','akhil@gmail.com', 'kochi')
    cursor.execute(query, values)
    connection.commit()


    # UPDATE OPERATION
    query = """
            UPDATE students
            SET city = %s
            WHERE student_id = %s
            """
    values = ('thrissur', 106)
    cursor.execute(query, values)
    connection.commit()


    # DELETE OPERATION
    query = """
            DELETE FROM students
            WHERE student_id = %s
            """
    values = (106,)
    cursor.execute(query, values)
    connection.commit()


    # TRUNCATE OPERATION
    query = """
            TRUNCATE TABLE students
            """
    cursor.execute(query)
    connection.commit()


    #username=input()
    #password=input()

    #query=f"""SELECT * FROM users
             #WHERE username = %s 
             #AND password = %s"""

    #cursor.execute(query, (username, password))


except:
    print("Something went wrong")

finally:
    connection.close()
    print("operations completed")