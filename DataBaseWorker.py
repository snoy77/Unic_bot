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

def getAllSiteURL():
    DBPrit(0)
    DBPrit(1, "вернуть ссылку")
    try:
        with connect(
            host = TI.DB_host,
            user = TI.DB_login,
            password = TI.DB_password,
            database = TI.DB_name,
        ) as connection:
            print("Соединение успешно: " + str(connection))
            query_to_bd = "select goung_text, url from sites where name = \'" + site_name + "\'"
            with connection.cursor() as cursor:
                print("Запрос: \'" + query_to_bd + "\'...")
                cursor.execute(query_to_bd)
                print("Успешно")
                result = cursor.fetchall()
                print("Результат запроса:\n" + str(result))
                DBPrit(0)
                return result
    except Error as e:
        DBPrit(3, str(e))
    DBPrit(10)
    return False
def getSiteURL(site_name):
    DBPrit(0)
    DBPrit(1, "вернуть ссылку")
    try:
        with connect(
            host = TI.DB_host,
            user = TI.DB_login,
            password = TI.DB_password,
            database = TI.DB_name,
        ) as connection:
            print("Успешно: " + str(connection))
            query_to_bd = "select goung_text, url from sites where name = \'" + site_name + "\'"
            with connection.cursor() as cursor:
                print("Запрос: \'" + query_to_bd + "\'...")
                cursor.execute(query_to_bd)
                print("Успешно")
                result = cursor.fetchall()
                print("Результат запроса:\n" + str(result))
                DBPrit(10)
                return result[0]
    except Error as e:
        DBPrit(3, str(e))
    DBPrit(10)
    return False
