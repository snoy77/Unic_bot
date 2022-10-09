import serv.CommonServ as CS

#на 03.08.2022 модуль умеет считать только 2 числа одновременно
#   или запоминать последние числа, складывая со следующими
operators = ['+','-','*','/']
operator = ''
last_result = 0

#-------------- шаблонные свойства и методы для микросвервисов -------------
Trigers_words = ['посчитай ']

#является ли сообщение запросом для этого модуля.
def isItToMe(message_text):
    global operator
    message_text = message_text.lower()


    #Если есть тригерное слово - сразу определяем этот модуль
    for triger_word in Trigers_words:
        if not message_text.find(triger_word) == -1:
            return True

    #Проверим на формат: должен быть оператор, и с двух сторон или с правой стороны число
    message_text = CS.deleteTrigerWord(Trigers_words, message_text)
    message_words = False

    #найдёмм оператор и поделим текст
    for e in operators:
        if not message_text.find(e) == -1:
            operator = e
            message_words = message_text.split(e)

    #найдём числа
    if message_words == False:
        return False

    for e in range(0, len(message_words)):
        message_words[e].lstrip()
        message_words[e].rstrip()
        if CS.is_number(message_words[e]) == False:
            return False
    return True


def setAnswerObject(message_text, AnswerObject):
    global operator
    AnswerObject.text = 'Я пока так не умею, прости...'

    #Уберём слово-тригер и отформатируем сообщение
    #!!! Знак "?" для этого модуля не рекомуендуется удалять
    message_text = message_text.lower()
    for e in operators:
        if not message_text.find(e) == -1:
            operator = e

    if operator == '':
        AnswerObject.text = 'Я не нашёл тут алгоритмического знака...'
        return AnswerObject
    digits = message_text.split(operator)
    digits_list = []

    for i in range(0, len(digits)):
        digits[i].lstrip()
        digits[i].rstrip()
        digits_list.append(float(digits[i]))

    if operator == '+':
        res = digits_list[0] + digits_list[1]
    elif operator == '/':
        res = digits_list[0] / digits_list[1]
    elif operator == '*':
        res = digits_list[0] * digits_list[1]
    elif operator == '-':
        res = digits_list[0] - digits_list[1]

    AnswerObject.text = "= " + str(res)
    operator = ''
    return AnswerObject
#---------------------------------------------------------------------------
