#!/usr/bin/env python3

import random
import string

def open_my_pass_dict():
    f = open("my_password.txt", "r")
    str_from_my_password = f.read()
    f.close()

    my_pass_dict = eval(str_from_my_password.replace("'", "\""))
    return my_pass_dict

def my_pass():
    service = input('Введите название сервиса, для которого будет создан пароль: ')
    pass_length = int(input('Укажите желаемую длину пароля: '))

    password = "".join(random.choices(string.printable[:62], k=pass_length))

    f = open("my_password.txt", "r")
    str_from_my_password = f.read()
    f.close()

    my_pass_dict = eval(str_from_my_password.replace("'", "\""))

    my_pass_dict[service] = password

    f = open("my_password.txt", "w")
    f.write(str(my_pass_dict))
    f.close()

    return f"Пароль для '{service}' == '{password}'"

def my_services():
    f = open("my_password.txt", "r")
    str_from_my_password = f.read()
    f.close()

    my_pass_dict = eval(str_from_my_password.replace("'", "\""))
    [ print(i) for i in my_pass_dict ]

def my_service_pass():
    service = input('Введите название сервиса, чтобы получить пароль: ')
    f = open("my_password.txt", "r")
    str_from_my_password = f.read()
    f.close()

    my_pass_dict = eval(str_from_my_password.replace("'", "\""))

    return f"пароль от {service} == {my_pass_dict[service]}"
