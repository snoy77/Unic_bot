import BotStatusPrinter as BSP
import telegainfo as TI
import discord
from discord.ext import commands

import serv.MathModule as MM
import QueryAndAnsver as QA

_moduleName = 'Discord_Main'
config = TI.dis_config


intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True


BSP.ModuleMes(_moduleName, 'Дискорд-соединение...')
bot = commands.Bot(command_prefix = TI.dis_config['prefix'], intents=intents)

BSP.ModuleMes(_moduleName, 'Дискорд-соединение... УСПЕХ')

BSP.ModuleMes(_moduleName, 'Инициализация модуля...')

@bot.event
async def on_ready():
    BSP.ModuleMes(_moduleName, 'Запуск бота... УСПЕХ')
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def calc(ctx, *, text):

    answer = QA.AnswerClass()

    #print(ctx.message)
#    def check(message):
        # если автор ожидаемого сообщения - автор команды nhw, то это сообщение можно принять
        # проверка нужна, чтобы другие пользователи не мешали выполнению команды своими сообщениями
#        if message.author == ctx.author:
#            return message
#    dd = await bot.wait_for('message', check=check)
    print(text)
    MM.setAnswerObject(text, answer)

    await ctx.send(answer.text)

def StartModule():
    global _moduleName
    global bot

    BSP.ModuleMes(_moduleName, 'Запуск бота...')
    #try:
    bot.run(TI.dis_config['token'])
    #except:
    #    BSP.ModuleMes(_moduleName, 'Запуск бота...ПРОВАЛ: пока не написан функционал')

    print()

BSP.ModuleMes(_moduleName, 'Инициализация модуля... УСПЕХ')
