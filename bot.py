#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import urllib3

from telegram.ext import Updater, CommandHandler

TOKEN='748030895:AAGshtffnUAGrFKUBI-rOOA3fKrxfoVldtw'
# REQUEST_KWARGS={
#     'proxy_url': 'https://190.151.10.226:8080/',
#     # Optional, if you need authentication:
# }

def start_bot(bot, updtr):
    print('Вызван /start')
    mytext = """Привет пользователь!!!!

    Я простой бот и понимаю только одну комманду /start
    """
    updtr.message.reply_text(mytext)

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_bot))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()