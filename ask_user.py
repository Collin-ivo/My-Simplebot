#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

answers = {
    'привет': 'Привет!',
    'Привет': 'Привет!',
    'как дела': 'Отлично а у тебя?',
    'Как дела': 'Отлично а у тебя?',
    'как дела?': 'Отлично а у тебя?',
    'пока': 'Еще увидимся!',
    'Пока': 'Еще увидимся!'
}

def ask_user(answers):
    try:
        while True:
            user_input = input('Скажи что нибудь: ')
            answer = get_answer(user_input, answers)
            if answer == None:
                print('Я глупый бот и не очень то многое понимаю!')
                continue
            print(answer)

            if user_input == 'пока' or user_input == 'Пока':
                break
    except KeyboardInterrupt:
        print('\nВсего хорошего!')
        sys.exit(1)




def get_answer(question, answers):
    return answers.get(question)

if __name__ == '__main__':
    ask_user(answers)