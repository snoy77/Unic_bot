#Модуль осуществляет поиск запросов из списка запросов и выдачу овтета на них


QueryAndAnsver = [
#0 - варианты запроса для овтета
#1 - ответ на варианты запроса
[["ответ"], "ответ"],
[["0"], "1"]

]

def returnfastAnsver(message_text):
    #Форматируем текст сообщения для првоерки
    message_text =  message_text.lower().replace('?','')
    #Проверяем сообщение на наличие в запросе
    for Q in QueryAndAnsver:
        if message_text in Q[0]:
            #Возвращаем список параметров ответа (в будущем будет больше параметров)
            return [Q[1]]