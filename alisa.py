#!/usr/bin/env python3

from bash import about_comp, git3, music, tsr
from birthday_count_days import bcd
from how_are_you import how_are_you as h
from my_pass import my_pass, my_services, my_service_pass
from weather import weather as w
from what_time import what_time as wt
from ya_short_2 import question2alisa as q2a

DATABASE = {
    'Саня': 'Будапешт',
    'Соня': 'Москва',
    'Юлия': 'Мытищи',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'

def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Алиса':
        return process_alisa(elements[1])
    elif elements[0] in DATABASE:
        return process_friend(elements[0], elements[1])
    else:
        return "<неизвестный запрос>"

def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            city = DATABASE[name]
            return f"{name} в городе {city}"
        else:
            return "<неизвестный запрос>"
    else:
        return f"У тебя нет друга по имени {name}"


def process_alisa(query):
    if query[-1] == '?':
        query = query[:-1]
    query = query.lower()
    if query == 'сколько у меня друзей':
        count = len(DATABASE)
        format_friends_count(count)
        return f'У тебя {format_friends_count(count)}.'
    elif query == 'жд':
        return about_comp()
    elif query == 'апдейт на гит':
        return git3()
    elif query == 'музыка':
        return music()
    elif query == 'включи тэйлор свифт':
        return tsr()
    elif query == 'погода':
        return w()
    elif query == 'придумай пароль':
        return my_pass()
    elif query == 'список сервисов':
        return my_services()
    elif query == 'подскажи пароль':
        return my_service_pass()
    elif query == 'как дела':
        return h()
    elif query == 'который час':
        print('В каком городе?')
        city = input()
        return wt(city)
    elif query == 'сколько дней со дня рождения':
        year = int(input('год: '))
        month = int(input('месяц: '))
        day = int(input('день: '))
        return bcd(year, month, day)
    elif query == 'кто все мои друзья':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return q2a(query)


print('Привет, я - Алиса!')
print('Какой у вас вопрос?')

print(process_query(input('Ввод (Алиса, ...?): ')))
