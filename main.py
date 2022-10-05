#import telega_main
import BotStatusPrinter as BSP
import DataBaseWorker as DB
import telega_main
import threading

telega_tread = threading.Thread(target=telega_main.StartModule)

def StartAll():
    global telega_tread
    #Сообщение о запуске бота
    BSP.SystemPrint('Запуск бота...')
    DB.StartModule()

    #запуск чат потоков
    #telega_main.StartModule()
    telega_tread.start()

    print()
    BSP.SystemPrint('Модули активированы')



StartAll()
while True:
    pass

    BSP.SystemPrint('РАБОТА БОТА НАЧАЛАСЬ')
    k = input()
    #if k == "":
    #    StartAll()
