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
    #with connection.cursor() as cursor:
       # cursor.execute("SELECT * FROM students")
        #records=cursor.fetchall()
        #records=cursor.fetchone()
        #records=cursor.fetchmany(3)
        #print (records)

    with connection.cursor() as cursor:
        # query="""
        #     ALTER TABLE students
        #     ADD COLUMN phone VARCHAR(15) NOT NULL DEFAULT '11111111'
        #     """
        # cursor.execute(query)
        # Print("column added successfully")

        # query="DESC students"
        # cursor.execute(query)
        # # connection.commit()
        # result=cursor.fetchall()
        # for col in result:
        #     print(col)


        # query="""
        #      ALTER TABLE students
        #      MODIFY phone INT DEFAULT '11111111'
        #      """
        #  cursor.execute(query)
        #  Print("column added successfully")
        #  query="DESC students"
        #  cursor.execute(query)
        #  connection.commit()
        #  result=cursor.fetchall()
        #  for col in result:
        #      print(col)


        # query="""
        #       ALTER TABLE students
        #       RENAME COLUMN phone TO contact_number
        #      """
        #   cursor.execute(query)
        #   Print("column added successfully")
        #   query="DESC students"
        #   cursor.execute(query)
        #   connection.commit()
        #   result=cursor.fetchall()
        #   for col in result:
        #       print(col)



    query="""
              ALTER TABLE students
               DROP COLUMN contact_number
              """
           cursor.execute(query)
           Print("column added successfully")
           query="DESC students"
           cursor.execute(query)
           connection.commit()
           result=cursor.fetchall()
           for col in result:
               print(col)
        
except Exception as e:
    print(f")  Error occured: {e}")

finally:
    connection.close()
    print("operations completed") 



        #query = f"""SELECT * FROM students WHERE city = 'kochi'"""
        #cursor.execute(query)
        #result = cursor.fetchall()
        #print(result)

        #for record in records:
            #print(record)


     #user_input=" OR '1'='1"
     #query = f"""SELECT * FROM users WHERE s_name = '{user_input}' """
     #cursor.execute(query)
     #print(cursor.fetchall())



    #query= """
           #INSERT INTO students VALUES (%s, %s, %s,%s)
           #"""
    #values = (106, 'akhil','akhil@gmail.com', 'kochi')
    #cursor.execute(query, values)
    #connection.commit()

    #update delete truncate insert

    #username=input()
    #password=input()
     
    #query=f"""SELECT * FROM users
             #WHERE username = %s 
             #AND password = %s"""

    #cursor.execute(query, (username, password))          

         