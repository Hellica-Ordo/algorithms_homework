"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
from pympler import asizeof
from random import randint
from numpy import array
import hashlib
from uuid import uuid4

# """СЛОТЫ В ООП"""
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

first_worker = Worker('Olga', 'Timofeeva', 'CEO', 35000, 15000)
print(f"Класс без использования слотов использует {asizeof.asizeof(first_worker)} MiB памяти.")

class Worker:
    __slots__ = ['name', 'surname', 'position', '_income', 'wage', 'bonus']
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

first_worker = Worker('Olga', 'Timofeeva', 'CEO', 35000, 15000)
print(f"Класс c использованием слотов использует {asizeof.asizeof(first_worker)} MiB памяти.")

"""ВЫВОДЫ:
Использование slots позволяет хранить атрибуты класса в кортеже, который занимает меньше памяти. Список атрибутов при этом нельзя изменять "на лету", что может
не подходить для всех случаев, но вместе с тем это эффективный способ сократить использование памяти."""


# """ИНСТРУМЕНТЫ NUMPY"""
nums = [randint(-9000, 9000) for i in range(3000)]

def optimized_func_1(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

def optimized_func_array(nums):
    return array([i for i in range(0, len(nums), 2)])

print(f"Функция c использованием list занимает {asizeof.asizeof(optimized_func_1(nums))} MiB памяти.")
print(f"Функция c использованием array занимает {asizeof.asizeof(optimized_func_array(nums))} MiB памяти.")

"""ВЫВОДЫ:
Использование специализированного объекта array позволяет снизить количество используемой памяти. Это доказывает нам, что для работы с различными задачами стоит использовать 
специализированные билиотеки, потому что решения, собранные в них, обычно являются наиболее оптимизированными."""


#"""УДАЛЕНИЕ ССЫЛОК"""
url_hash_dict = {}

@profile
def url_cash():
    url = input('Пожалуйста, введите url-адрес: ')
    salt = uuid4().hex
    url_hash = hashlib.sha256(salt.encode() + url.encode('utf-8')).hexdigest()
    if url_hash_dict.get(url_hash):
        print(url_hash_dict[url_hash])
    else:
        url_hash_dict.setdefault(url, url_hash)

print(f"Функция без удаления ссылок занимает {asizeof.asizeof(url_cash())} MiB памяти.")

@profile
def url_cash_opt():
    url = input('Пожалуйста, введите url-адрес: ')
    salt = uuid4().hex
    url_hash = hashlib.sha256(salt.encode() + url.encode('utf-8')).hexdigest()
    if url_hash_dict.get(url_hash):
        print(url_hash_dict[url_hash])
    else:
        url_hash_dict.setdefault(url, url_hash)
    del salt
    del url

print(f"Функция c удалением ссылок занимает {asizeof.asizeof(url_cash())} MiB памяти.")

"""ВЫВОДЫ:
На данном примере не очень наглядно, но тем не менее удаление ссылок на уже отработавшие переменные позволяет снизить затраты памяти, при этом
не нарушая работу функции. Я думаю, это наиболее актуально для функций или классов с большим количеством переменных."""