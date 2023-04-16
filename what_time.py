#!/usr/bin/env python3

import datetime as dt

UTC_OFFSET = {
    'Плимут': 1,
    'Санкт-Петербург': 3,
    'Москв': 3,
    'Самар': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казан': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уф': 5,
    'Красноярск': 7,
    'Перм': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def city_name(city):
    if city[-1] in ['е', 'а', 'и', 'ь']:
        city = city[:-1]
    return city

def what_time(city):
    city = city_name(city)
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city
    utc_time = dt.datetime.utcnow()
    period = dt.timedelta(hours = UTC_OFFSET[city])
    return (utc_time + period).strftime("%H:%M")
