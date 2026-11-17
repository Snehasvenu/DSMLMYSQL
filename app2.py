print(connection._dict__)


try:
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        records=cursor.fetchall()

        #print records
        for record in records:
            print(record)

except:
    print("Something went wrong")        