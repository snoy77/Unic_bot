import serv.CommonServ as CS

#на 03.08.2022 модуль умеет считать только 2 числа одновременно
#   или запоминать последние числа, складывая со следующими
operators = ['+','-','*','/']
operator = ''
last_result = None

#-------------- шаблонные свойства и методы для микросвервисов -------------
Trigers_words = ['посчитай ']

#является ли сообщение запросом для этого модуля.
def isItToMe(message_text):
    global last_result

    message_text = message_text.lower()


    #Если есть тригерное слово - сразу определяем этот модуль
    for triger_word in Trigers_words:
        if not message_text.find(triger_word) == -1:
            return True

    #Проверим на формат: должен быть оператор, и с двух сторон или с правой стороны число
    message_text = CS.deleteTrigerWord(Trigers_words, message_text)
    message_words = False

    #найдёмм оператор и поделим текст
    operator = ''
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

    #Сообщение о том, почему бот не может посчитать то или иное выражение, будем составлять в обработке постройки ответа setAnswerObject()
    if (CS.is_number(message_words[1]) or message_words[1] == '') and (message_words[0] == '' or CS.is_number(message_words[0])):
        return True
    return False

def setAnswerObject(message_text, AnswerObject):
    #определяем переменные
    global last_result

    operator = ''
    message_words = None
    AnswerObject.text = 'Я пока так не умею, прости...'

    #Уберём слово-тригер и отформатируем сообщение
    #!!! Знак "?" для этого модуля не рекомуендуется удалять

    message_text = message_text.lower()
    message_text = CS.deleteTrigerWord(Trigers_words, message_text)
    for e in operators:
        if not message_text.find(e) == -1:
            operator = e
    if operator == '':
        AnswerObject.text = 'Я не нашёл тут алгоритмического знака...'
        return AnswerObject

    #Уберём лишние пробелы для чисел
    message_words = message_text.split(e)
    for e in range(0, len(message_words)):
        message_words[e].lstrip()
        message_words[e].rstrip()

    digits = message_text.split(operator)
    if digits[1] == '':
        AnswerObject.text = 'Второе число не может быть пустым. Пожайлуйста, введи там хотя бы \"0\", чтобы я понимал...'
        return AnswerObject
    if digits[0] == '' and last_result == None:
        digits[0] = '0'
    elif digits[0] == '' and last_result != None:
        digits[0] = last_result
    #digits_list = []

    for i in range(0, len(digits)):
        digits[i].lstrip()
        digits[i].rstrip()
        digits[i] = float(digits[i])

        #digits_list.append(float(digits[i]))

    if operator == '+':
        res = digits[0] + digits[1]
    elif operator == '/':
        res = digits[0] / digits[1]
    elif operator == '*':
        res = digits[0] * digits[1]
    elif operator == '-':
        res = digits[0] - digits[1]

    last_result = str(res)#переводим в строку, чтобы удобнее было алгоритму сразу обрабатывать строки
    AnswerObject.text = "= " + str(res)
    operator = ''
    return AnswerObject
#---------------------------------------------------------------------------
