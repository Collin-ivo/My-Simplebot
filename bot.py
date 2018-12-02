#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, urllib3, datetime, ephem

import settings


from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

import logging

logging.basicConfig(handlers=[logging.FileHandler('bot.log', encoding='utf-8')],
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )



def start_bot(bot, update):
    mytext = "Привет {}!!!! Напиши свой возраст".format(update.message.chat.first_name)
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def planet_chat(bot, update):
    mytext = "Что бы узнать в каком созвездии сейчас находится планета, напиши ее название"
    logging.info('Пользователь {} нажал /planet'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def chat(bot, update):
    try:
        text = int(update.message.text)
        logging.info(str(text))
        if text <= 6:
            deal = 'Свсем мал еще, в детский садик ходишь а уже в сети чатишься с ботом...'
        elif text <= 15:
            deal = 'Школоло =)'
        elif text <= 20:
            deal = 'Учишься в ВУЗе значит'
        else:
            deal = 'Работаешь на работе значит'
        update.message.reply_text(deal)
    except TypeError:
        update.message.reply_text('Введи свой полный возраст в цифрах!')




def main():
    updater = Updater(settings.TELEGRAM_API_KEY)

    updater.dispatcher.add_handler(CommandHandler("start", start_bot))
    updater.dispatcher.add_handler(CommandHandler("planet", planet_chat))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    logging.info("Bot started")
    main()