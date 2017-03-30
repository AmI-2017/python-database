import pymysql

if __name__ == "__main__":
    connection = pymysql.connect(user="root",password="root",database="todolist",host="localhost")

    sql = "insert into todo (description, deadline) values (%s, %s)"
    my_description = "be happy"
    my_date = "2017-04-05"

    cursor = connection.cursor()
    cursor.execute(sql, (my_description, my_date) )
    connection.commit()
    cursor.close()

    sql2 = "SELECT description, deadline FROM todo"
    curs2 = connection.cursor()
    curs2.execute(sql2)
    result = curs2.fetchall()
    print(result)

    connection.close()

    for row in result:
        print(row[0])