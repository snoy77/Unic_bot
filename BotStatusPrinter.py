import telegainfo as TI

def printStatusBot(message_data, user, chat, message_text, mesType):
    if mesType == 0:
        print(getChatTemples(chat) + getUserTemples(user) + " << " + message_text)
    elif mesType == 1:
        print(getChatTemples(chat) + getUserTemples(user) + " >> " + message_text)
    elif mesType == 2:
        print(getChatTemples(chat) + getUserTemples(user) + " == " + message_text)
def getChatTemples(chat):
    return '[' +  str(chat) + ']'
def getUserTemples(user):
    return '{' +  str(user) + '}'

def stopForDebug(individualStop, status_text = '', anywayWriteStatus = 1):
    if TI.debug_mod == 1 or individualStop == 1:
        input('!!! Остановка дебага: - ' + status_text)
        return
    if anywayWriteStatus == 1:
        print(status_text)


def ModuleMes(moduleName, mes):
    print(' ' + moduleName + ': ' + mes)
def SystemPrint(mes):
    print(' MainModule: ' + mes)

def SystemUnnowErrorPrint():
    print('\n -----------------------------------------------------------------------------------')
    print(' SYS ERROR: Работа бота прекращена по непредвиденным обстоятельствам. Перезагрузить?')
    print(' -----------------------------------------------------------------------------------')
