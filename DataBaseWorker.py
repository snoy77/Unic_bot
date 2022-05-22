import mysql.connector
import telegainfo as TI
from mysql.connector import connect, Error

def getAllSiteURL():
    print("Попытка подсоединения к базе: вернуть ссылку")
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
                cursor.execute(query_to_bd)
                result = cursor.fetchall()
                print("Результат запроса:\n" + str(result))
                return result
    except Error as e:
        print(e)
        a = input()
    return False
def getSiteURL(site_name):
    print("Попытка подсоединения к базе: вернуть ссылку")
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
                cursor.execute(query_to_bd)
                result = cursor.fetchall()
                print("Результат запроса:\n" + str(result))
                return result[0]
    except Error as e:
        print(e)
        a = input()
    return False
