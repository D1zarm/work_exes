import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        curcorclass = pymysql.cursors.DictCursor
    )
    print("Соединение установлено!")

    try:
        #Создание таблицы
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE 'users'(id int AUTOINCREMENT, name varchar(32), password varchar(32), PRIMARY_KEY(id));"
            cursor.execute(create_table_query)
            print("Таблица создана успешно!")

        #Добавление данных в таблицу
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO 'users' (name, password) VALUES ('Иван','12345')"
            cursor.execute(insert_query)
            connection.commit()

        #Вывод всех данных таблицы
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM 'users'")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        #Обновление данных в таблице
        with connection.cursor() as cursor:
            update_query = "UPDATE 'users' SET name = 'Петр' WHERE id = 1"
            cursor.execute(update_query)
            connection.commit()

        #Удаление данных 
        with connection.cursor() as cursor:
            delete_query = "DELETE FROM 'users' WHERE id = 1"
            cursor.execute(delete_query)
            connection.commit()
    finally:
        connection.close()


except Exception as ex:
    print("Соединение не удалось")
    print(ex)
