import mysql.connector
import telegainfo as TI
from mysql.connector import connect, Error

def DBPrit(print_id, mes = ""):
    if print_id == 0:
        print("\n----------------MySQL----------------\n")
    elif print_id == 10:
        print("\n================MySQL================\n")
    elif print_id == 1:
        print("Попытка подсоединения к базе: " + mes)
    elif print_id == 2:
        print("Ошибка: " + mes)
    elif print_id == 3:
        print("Ошибка: " + mes)
        input("Остановка работы по ошибке...")


def return_query_result(query_to_bd):
    DBPrit(0)
    try:
        with connect(
            host = TI.DB_host,
            user = TI.DB_login,
            password = TI.DB_password,
            database = TI.DB_name,
        ) as connection:
            print("> Успешно: " + str(connection))
            with connection.cursor() as cursor:
                print("> Запрос: \'" + query_to_bd + "\'...")
                #Поулчаем резульатт по запросу
                cursor.execute(query_to_bd)
                #перерабатываем ег ов список
                result = cursor.fetchall()

                print("> Успешно: " + str(cursor.rowcount) + " строк")
                print("> Результат запроса:\n" + str(result))

                DBPrit(10)
                if cursor.rowcount == 0:
                    return False
                else:
                    return result
    except Error as e:
        DBPrit(3, str(e))
    DBPrit(10)
    return False
