"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

import hashlib

def save_into_file(password_hash):
    with open('password_library.txt', 'w') as file:
        file.write(str(password_hash))

def read_file():
    with open('password_library.txt', "r") as file:
        stored_hash = str(file.read())
        return stored_hash

def hashing(text):
    password_salt = input('Пожалуйста, введите логин:')
    return hashlib.sha256(input(text).encode() + password_salt.encode())

def create_password():
    hash_pass = hashing("Пожалуйста, введите пароль: ")
    save_into_file(hash_pass.hexdigest())
    return hash_pass

def check_password():
    hash_in_file = read_file()
    hash_current = hashing("Пожалуйста, введите пароль, заданный при регистрации: ")
    if str(hash_current.hexdigest()) == hash_in_file:
        print("Авторизация пройдена, добро пожаловать.")
    else:
        print("Неверный логин или пароль.")

create_password()
check_password()