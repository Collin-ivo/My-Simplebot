#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import urllib3
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


TOKEN = '748030895:AAGshtffnUAGrFKUBI-rOOA3fKrxfoVldtw'


def start_bot(bot, update):
    mytext = "Привет {}!!!! Я простой бот и понимаю только одну комманду {}".format(update.message.chat.first_name, '/start')
    update.message.reply_text(mytext)

def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    logging.info("Bot started")
    main()