#!/usr/bin/env python3

from datetime import date

def bcd(year=1973, month=10, day=30):
    birthday = date(year, month, day)
    today = date.today()
    duration = (today - birthday)

    return duration
