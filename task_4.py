"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

def pull_my_dict():
    my_dict = {}
    for i in range(1000):
        my_dict[i] = i
    return my_dict

def pull_ordered_dict():
    ordered_dict = OrderedDict()
    for i in range(1000):
        ordered_dict[i] = i
    return ordered_dict

def getitem_my_dict(my_dict, n):
    return my_dict[n]

def getitem_ordered_dict(ordered_dict, n):
    return ordered_dict[n]

my_dict = pull_my_dict()
ordered_dict = pull_ordered_dict()
n = 75

print('Операции с обычным словарём: pull, getitem:')
print(timeit("pull_my_dict()", globals = globals(), number = 10000))
print(timeit("getitem_my_dict(my_dict, n)", globals = globals(), number = 10000))
print('Операции с OrderedDict: pull, getitem:')
print(timeit("pull_ordered_dict()", globals = globals(), number = 10000))
print(timeit("getitem_ordered_dict(ordered_dict, n)", globals = globals(), number = 10000))

"""ВЫВОДЫ:
В сравнении с обычным словарём в Python 3.8 OrderedDict немного медленнее. С учётом того, что в Python 3.6 и и новее словари по умолчанию стали упорядоченными,
я не вижу смысла использовать OrderedDict, кроме как в проектах, написанных на старых версиях Python."""