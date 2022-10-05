import telebot
from telebot import types

import random as rand

import BotStatusPrinter as BSP
import telegainfo as TI
import QueryAndAnsver as QA

_moduleName = 'telega_main'


#----------------Инициализаци первых данных----------------
ADMIN_ID = 1182327310
BSP.ModuleMes(_moduleName, 'Телеграм-соединение...')
bot = telebot.TeleBot(TI.token)
BSP.ModuleMes(_moduleName, 'Телеграм-соединение... УСПЕХ')



BSP.ModuleMes(_moduleName, 'Инициализация функций...')


def StartModule():
    global bot
    global _moduleName

    #----------------Запуск бота----------------
    BSP.ModuleMes(_moduleName, 'Чат -- ЗАПУСК')
    bot.polling(none_stop=True, interval=0)
    BSP.ModuleMes(_moduleName, 'Чат -- ПРЕКРАЩЕНИЕ РАБОТЫ')
    BSP.stopForDebug(1)

#----------------Определение некоторых методов----------------
def getMessageChatMainInfo(chat):
    return str(chat.id) + ' ' + str(chat.username) + ' ' + str(chat.title)
def getMessageUserMainInfo(user):
    return str(user.id) + ' ' + str(user.first_name) + ' ' + str(user.last_name)


#----------------Определение событий----------------


@bot.message_handler(commands=['debagon', 'debagoff'])
def debag_enable(message):
    #------Шаблон первичных данных------
    chat_id = message.chat.id
    message_text = message.text
    message_data = message.date
    message_user = getMessageUserMainInfo(message.from_user)
    message_chat = getMessageChatMainInfo(message.chat)
    BSP.printStatusBot(message_data, message_user, message_chat, message_text, 0)

    if message.from_user.id == ADMIN_ID:
        if message_text == '/debagoff':
            BSP.stopAll = 0
            going_message = 'Режим дебага выключен'
            BSP.printStatusBot(message_data, message_user, message_chat, 'Выключен режим дебага', 2)
        elif message_text == '/debagon':
            BSP.stopAll = 1
            going_message = 'Режим дебага включен'
            BSP.printStatusBot(message_data, message_user, message_chat, 'Включен режим дебага', 2)

        bot.send_message(chat_id, going_message)
        BSP.printStatusBot(message_data, message_user, message_chat, going_message, 1)
    else:
        BSP.printStatusBot(message_data, message_user, message_chat, 'Пользователь не админ бота, игнорю', 2)

@bot.message_handler(content_types=['text'])
def message_going(message):
    BSP.stopForDebug(0, "message_going началоif", 0)

    chat_id = message.chat.id
    message_text = message.text
    message_data = message.date
    message_user = getMessageUserMainInfo(message.from_user)
    message_chat = getMessageChatMainInfo(message.chat)
    BSP.printStatusBot(message_data, message_user, message_chat, message_text, 0)

    BSP.stopForDebug(0, "message_going - Попытка отправки ответа...", 0)
    #--------------------------переделка--------------------------

    if message_text.lower().replace('?','') in ['жив', 'живой', "ты жив"]:
        going_message = "Агась"
        bot.send_message(chat_id, going_message)
        bot.send_sticker(chat_id, 'CAACAgEAAxkBAAPkYn5t2aAkAAGiipkFKzpGvXz4bsUcAAJaAAPArAgjmrw81VndF8IkBA')
    else:
        answer_object = QA.returnAnswer(message_text)
        going_message = answer_object.text
        bot.send_message(chat_id, going_message)
    #-------------------------------------------------------------
    #fastAnsver = QA.returnfastAnsver(message_text)
    #if fastAnsver != False:
    #    going_message = fastAnsver[0]
    #    bot.send_message(chat_id, going_message)
    #else:
    #    if message_text.lower().replace('?','') in ['жив', 'живой', "ты жив"]:
    #        going_message = "Агась"
    #        bot.send_message(chat_id, going_message)
    #        bot.send_sticker(chat_id, 'CAACAgEAAxkBAAPkYn5t2aAkAAGiipkFKzpGvXz4bsUcAAJaAAPArAgjmrw81VndF8IkBA')
    #    else:
    #        going_message = 'Не понял, разъясни почётче...'
    #        bot.send_message(chat_id, going_message)

    BSP.printStatusBot(message_data, message_user, message_chat, going_message, 1)

    BSP.stopForDebug(0, "message_going Конец", 0)

BSP.ModuleMes(_moduleName, 'Инициализация функций... УСПЕХ')
