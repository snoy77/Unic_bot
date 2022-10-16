def deleteTrigerWord(Trigers_words, message):
    for e in Trigers_words:
        message.replace(e, '')
    return message

#https://all-python.ru/osnovy/proverka-na-chislo.html
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
