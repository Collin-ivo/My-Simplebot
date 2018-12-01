#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import urllib3
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
    mytext = "Привет {}!!!! Я простой бот и понимаю только одну комманду {}".format(update.message.chat.first_name, '/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(mytext)

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    updater = Updater(settings.TELEGRAM_API_KEY)

    updater.dispatcher.add_handler(CommandHandler("start", start_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    logging.info("Bot started")
    main()