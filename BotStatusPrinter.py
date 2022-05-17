#input('Инициализация модуля BSP')
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
#input('Инициализация модуля BSP')
#Функция для дебага или просто вывода статуса. Останавливает индивидуально строку,
    #или же все строки при инциализации дебага в начале
stopAll = int(input("Режим дебага? Введите 1 (да) или 0 (нет):\n"))
def stopForDebug(individualStop, status_text = '', anywayWriteStatus = 1):
    if stopAll == 1 or individualStop == 1:
        input('!!! Остановка дебага: - ' + status_text)
        return
    if anywayWriteStatus == 1:
        print(status_text)
