#import telega_main
import BotStatusPrinter as BSP
import DataBaseWorker as DB
import telega_main
import discord_main as DIS_MAIN
import threading

_telega_thread = None
_discord_thread = None

def thread_init():
    global _telega_thread
    global _discord_thread

    _telega_thread = threading.Thread(target = telega_main.StartModule)
    _discord_thread = threading.Thread(target = DIS_MAIN.StartModule)
def thread_start():
    global _telega_thread
    global _discord_thread

    _telega_thread.start()
    _discord_thread.start()

def StartAll():
    global _telega_tread
    global _discord_thread

    print()
    BSP.SystemPrint('Запуск внешних сред чатинга...')
    print('-----------------------------------------------')

    DB.StartModule()

    #запуск чат-потоков
    thread_start()


thread_init()
StartAll()



while True:
    pass

    print('\n=============== РАБОТА БОТА НАЧАЛАСЬ ===============')
    k = input()
