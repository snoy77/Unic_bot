#Модуль осуществляет поиск запросов из списка запросов и выдачу овтета на них
import DataBaseWorker as DBW


def findSiteUrl(arguments):
    site_name = arguments[0]
    result = DBW.getSiteURL(site_name)
    if result == False:
        return 'Не знаю такой сайт'
    else:
        return '[' + result[0] + '](' + result[1] + ')'

QueryAndAnsver = [
#0 - варианты запроса для овтета
#1 - ответ на варианты запроса
[["ответ"], "ответ"],
[["0"], "1"],
[["гитхаб", "гит", "твой гит", 'git', 'github'], findSiteUrl, ['git']],
[['мудл'], findSiteUrl, ['moodle']]
]

def returnfastAnsver(message_text):
    #Форматируем текст сообщения для првоерки
    message_text =  message_text.lower().replace('?','')
    #Проверяем сообщение на наличие в запросе
    for Q in QueryAndAnsver:
        if message_text in Q[0]:
            #Возвращаем список параметров ответа (в будущем будет больше параметров)
            if not isinstance(Q[1], list):
                Q[1] = [Q[1](Q[2])]
            return Q[1]
    return False
