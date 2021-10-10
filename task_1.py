"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time
from random import randint
from timeit import Timer

def benchmark(func):        #Декоратор, выводящий время, которое заняло выполнение декорируемой функции. Вызывать через @benchmark()
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'Функция {func.__name__}: {(end_time - start_time)} секунд.')
        return result
    return wrapper

my_list = []
my_dictionary = {}

#@benchmark
def append_to_list(number):  # O(1)    добавление элемента в список через append
    my_list.append(number)  # O(1)

#@benchmark
def add_to_dictionary(my_dictionary):      # O(1) добавление пары ключ-значение в словарь
    my_dictionary[f'Ключ {randint(0, 99000)} {chr(randint(0, 255))}'] = randint(0, 9000)    # O(1)

#@benchmark
def fill_my_list(my_list, lenght):          # O(n)      заполнение списка случайными значениями
    for i in range(lenght):                 # O(n)
        my_list.append(randint(0, 9000))    # O(1)

#@benchmark
def fill_my_dictionary(my_dictionary, lenght):        # O(n) заполнение словаря случайными значениями
    for i in range(lenght):                           # O(n)
        my_dictionary[f'Ключ {randint(0, 99000)} {chr(randint(0, 255))}'] = randint(0, 9000)    # O(1)

#@benchmark
def value_from_list(number):         # O(n)  получение значения из списка по индексу
    my_list[my_list.index(number)]   # О(n)

#@benchmark
def value_from_dictionary(number):     # O(1)
    my_dictionary.get(number)          # O(1)

# append_to_list(randint(0, 99000))
# add_to_dictionary(my_dictionary)
# fill_my_list(my_list, 15000)
# value_from_list(1)
# fill_my_dictionary(my_dictionary, 15000)
# value_from_dictionary(1)

t1 = Timer("append_to_list(10)", "from __main__ import append_to_list")
print("append_to_list: 10000 операций за", t1.timeit(number=10000), "секунд")

t2 = Timer("add_to_dictionary(my_dictionary)", "from __main__ import add_to_dictionary, my_dictionary")
print("add_to_dictionary: 10000 операций за", t2.timeit(number=10000), "секунд")

t3 = Timer("value_from_list(10)", "from __main__ import value_from_list")
print("value_from_list: 10000 операций за", t3.timeit(number=10000), "секунд")

t4 = Timer("value_from_dictionary(10)", "from __main__ import value_from_dictionary")
print("value_from_dictionary: 10000 операций за", t4.timeit(number=10000), "секунд")

t5 = Timer("fill_my_dictionary(my_dictionary, 150)", "from __main__ import fill_my_dictionary, my_dictionary")
print("fill_my_dictionary: 10000 операций за", t5.timeit(number=10000), "секунд")

t6 = Timer("fill_my_list(my_list, 150)", "from __main__ import fill_my_list, my_list")
print("fill_my_list: 10000 операций за", t6.timeit(number=10000), "секунд")

"""
Вместо того, чтобы получить время через декоратор, я воспользовалась методом с урока 4.

ВЫВОДЫ:
Заполнение списка происходит быстрее, чем заполнение словаря. Скорее всего, это связано с тем, что в словарь является хеш-таблицей, и система
высчитывает хеши всякий раз при добавлении нового элемента. При этом работа с элементами в словарях происходит на порядок быстрее, что опять же
связано с тем, что в словаре существует хеш. Я бы предположила, что с точки зрения быстродействия списки имеет смысл использовать для хранения
небольших объёмов постоянно изменяемых данных, в то время как словари подходят для постоянного хранения больших объёмов информации и работы с ней."""
