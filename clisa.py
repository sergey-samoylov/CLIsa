#!/usr/bin/env python3

from bash import about_comp, git3, music, tsr, news
from birthday_count_days import bcd
from how_are_you import how_are_you as h
# from my_pass import my_pass, my_services, my_service_pass
from weather import weather as w
from what_time import what_time as wt
from ya_short_2 import question2alisa as q2a

def process_clisa(query):
    if query[-1] == '?':
        query = query[:-1]
    query = query.lower()
    if query == 'жд':
        return about_comp()
    elif query == 'апдейт на гит':
        return git3()
    elif query == 'новости':
        return news()
    elif query == 'музыка':
        return music()
    elif query == 'включи тэйлор свифт':
        return tsr()
    elif query == 'погода':
        return w()
    elif query == 'как дела':
        return h()
    elif query == 'сколько дней со дня рождения':
        year = int(input('год: '))
        month = int(input('месяц: '))
        day = int(input('день: '))
        return bcd(year, month, day)
    else:
        return q2a(query)


print(process_clisa(input()))
