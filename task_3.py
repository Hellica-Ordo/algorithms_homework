"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from timeit import timeit
from collections import deque

def pull_list():
    my_list = list(range(1000))
    return my_list

def popleft_list(my_list):
    my_list = [1, 2, 3, 4, 5]
    my_list.pop(0)
    return my_list

def appendleft_list(my_list):
    my_list.insert(0, 10)
    return my_list

def extendleft_list(my_list):
    new_list = [1, 2, 3, 4, 5]
    for i, num in enumerate(new_list):
        my_list.insert(i, num)
    return my_list

def append_list(my_list):
    my_list.append(1)
    return my_list

def append_deque(my_deque):
    my_deque.append(1)
    return my_deque

def pull_deque():
    my_deque = deque(range(10000))
    return my_deque

def popleft_deque(my_deque):
    my_deque.popleft()
    return my_deque

def appendleft_deque(my_deque):
    my_deque.appendleft(10)
    return my_deque

def extendleft_deque(my_deque):
    new_list = [1, 2, 3, 4, 5]
    my_deque.extendleft(new_list)
    return my_deque

my_list = pull_list()
my_deque = pull_deque()

print('Операции с list: pull, popleft, append, appendleft, extend:')
print(timeit("pull_list()", globals = globals(), number = 10000))
print(timeit("popleft_list(my_list)", globals = globals(), number = 10000))
print(timeit("append_list(my_list)", globals = globals(), number = 10000))
print(timeit("appendleft_list(my_list)", globals = globals(), number = 10000))
print(timeit("extendleft_list(my_list)", globals = globals(), number = 10000))

print('Операции с deque: pull, popleft, append, appendleft, extend:')
print(timeit("pull_deque()", globals = globals(), number = 10000))
print(timeit("popleft_deque(my_deque)", globals = globals(), number = 10000))
print(timeit("append_deque(my_deque)", globals = globals(), number = 10000))
print(timeit("appendleft_deque(my_deque)", globals = globals(), number = 10000))
print(timeit("extendleft_deque(my_deque)", globals = globals(), number = 10000))

"""ВЫВОДЫ:
Заполнение deque происходит существенно медленнее, чем у list, но при этом deque быстрее выполняет операции со своими элементами, особенно в левой части.
Я бы рекомендовала использовать deque для хранения большиъ объёмов данных, к которым необходимо часто обращаться."""