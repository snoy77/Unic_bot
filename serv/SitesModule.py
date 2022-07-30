#Модуль дял работы с сайтами: запоминание ссылок, октрывание, и т.д.
import DataBaseWorker as DBW

_triger_word_add = ['добавь '] #Слова для добавления ссылки в список
_triger_word_open = ['открой '] #Слова для открытия ссылки
_triger_word_get = ['дай '] #Слова для запроса ссылки

sites_cash = []

def getSite(message_text, AnswerObject):
    global _triger_word_get

    #Удалим тригерные слова для этой команды
    for e in _triger_word_get:
        message_text.replace(e + " ", '')

    message_text = message_text.lstrip()
    message_text = message_text.rstrip()

    #Подготовим все аргументы для запроса
    arguments = []
    arguments.append(message_text)

    message_words = message_text.split(' ')
    try:
        message_words.remove(message_text)
    except:
        pass

    for word in message_words:
        arguments.append(word)

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

def addSiteToCash():
    pass


#-------------- шаблонные свойства и методы для микросвервисов -------------
Trigers_words = ['ссылку на', "ссылка на", "ссылочка на", "ссылочку на",
'сайт', "ссылк", "ссылку", "ссылочка", "ссылочку",
'ссылочк', 'сылк', 'сылочк']

#является ли сообщение запросом для этого модуля.
def isItToMe(message_text):
    message_text = message_text.lower()

    for triger_word in Trigers_words:
        if not message_text.find(triger_word) == -1:
            return True
    return False

def setAnswerObject(message_text, AnswerObject):

    AnswerObject.text = 'Я пока так не умею, прости...'

    #Уберём слово-тригер и отформатируем сообщение
    #!!! Знак "?" для этого модуля не рекомуендуется удалять
    message_text = message_text.lower()

    for e in Trigers_words:
        message_text = message_text.replace(e, '')

    #Опрееделяем к какой команде относится запрос
    for e in _triger_word_add:
        if not message_text.find(e) == -1:
            pass
    for e in _triger_word_open:
        if not message_text.find(e) == -1:
            pass

    #В ином случае это будет команда запроса ссылки
    getSite(message_text, AnswerObject)

#---------------------------------------------------------------------------