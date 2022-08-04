#Модуль осуществляет поиск запросов из списка запросов и выдачу овтета на них
import DataBaseWorker as DBW
import serv.SitesModule as SM
import serv.MathModule as MM

#------------- new algoritm ---------------------------
#объект ответа
class AnswerClass:
    text = 'Не понял, разъясни почётче...'

#Возвращает объект ответа
def returnAnswer(message_text):
    AnswerObject = AnswerClass()
    answer_methods = []

    #Опрос микросервисов на возможность ответа
    if SM.isItToMe(message_text):
        answer_methods.append(SM.setAnswerObject)
    if MM.isItToMe(message_text):
        answer_methods.append(MM.setAnswerObject)

    if len(answer_methods) == 1:
        #------ ВРЕМЕННАЯ ПУСТЫШКА -----------
        answer_methods[0](message_text, AnswerObject)
        #-------------------------------------

    return AnswerObject
#------------------------------------------------------


def findSiteUrl(arguments):
    site_name = arguments[0]
    result = DBW.getSiteURL(site_name)
    if result == False:
        return ['Не знаю такой сайт']
    else:
        return ['[' + result[0] + '](' + result[1] + ')']

QueryAndAnsver = [
#0 - варианты запроса для овтета
#1 - ответ на варианты запроса
[["ответ"], 0, ["ответ"]],
[["0"], 0, ["1"]],
[["гитхаб", "гит", "твой гит", 'git', 'github'], 1, 0, ['git']],
[['мудл'], 1, 0 , ['moodle']]
]
def returnFunctionObjectForIndex(index):
    if index == 1:
        return findSiteUrl
def returnfastAnsver(message_text):
    #Форматируем текст сообщения для првоерки
    message_text =  message_text.lower().replace('?','')
    #Проверяем сообщение на наличие в запросе
    for Q in QueryAndAnsver:
        if message_text in Q[0]:
            #Возвращаем список параметров ответа (в будущем будет больше параметров)
            if not isinstance(Q[2], list):
                Q[2] = returnFunctionObjectForIndex(Q[1])(Q[3])
            return Q[2]
    return False
