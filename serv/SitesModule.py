#Модуль дял работы с сайтами: запоминание ссылок, октрывание, и т.д.
import DataBaseWorker as DBW

#-------------- шаблонные свойства и методы для микросвервисов -------------
Trigers_words = ['ссылку на', "ссылка на", "ссылочка на", "ссылочку на",
'сайт', "ссылка", "ссылку", "ссылочка", "ссылочку"]

#является ли сообщение запросом для этого модуля.
def isItToMe(message_text):
    global _triger_word
    message_text = message_text.lower()
    message_words = message_text.split(' ')
    for triger_word in Trigers_words:
        if triger_word in message_words:
            _triger_word = triger_word
            return True
    return False

def setAnswerObject(message_text, AnswerObject):
    message_text = message_text.lower()

    #Уберём слово-тригер и приведём аргументы - все возможные варианты названия сайта
    #первый вариант
    message_text = message_text.replace(_triger_word, '')
    message_text = message_text.lstrip()
    message_text = message_text.rstrip()

    arguments = []
    arguments.append(message_text)

    message_words = message_text.split(' ')
    try:
        message_words.remove(message_text)
    except:
        pass

    for word in message_words:
        arguments.append(word)
    print("Слово тригер: " + _triger_word)

    #ПРЕОБРАЗОВАТЬ МОДУЛЬ ЗАПРОСОВ БАЗЫ ДАННЫХ
    #НА ПРОСТО ВЫПОЛНЕНИЕ ЗАПРОСОВ
    #ЗАПРОСЫ ПЕРЕДВАТЬ ОТ СЮДА ТУДА
    print(arguments)
    result = DBW.getSiteURL(arguments)

    if result == False:
        AnswerObject.text = 'Не знаю такой сайт'
    else:
        AnswerObject.text = ''
        for res in result:
            AnswerObject.text += '[' + res[0] + '](' + res[1] + ')\n'
#---------------------------------------------------------------------------
_triger_word = ""
sites_cash = []
def addSiteToCash():
    pass
