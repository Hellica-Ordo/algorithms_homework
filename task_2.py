"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""

import random

my_list = random.sample(range(0, 100), 10)

def min_value_square(my_list):                  #O(n^2)
    for i in my_list:                           #O(n)
        n = 0                                   #O(1)
        min_value = 100                         #O(1)
        while n < (len(my_list) - 1):           #O(n)
            if my_list[n] <= min_value:
                min_value = my_list[n]          #O(1)
            n += 1                              #O(1)
    return min_value                            #O(1)

print(my_list)
print(min_value_square(my_list))

def min_value_linear(my_list):                  #O(n)
        n = 0                                   #O(1)
        min_value = 100                         #O(1)
        while n < (len(my_list) - 1):           #O(n)
            if my_list[n] <= min_value:
                min_value = my_list[n]          #O(1)
                n += 1                          #O(1)
            else:
                n += 1                          #O(1)
        return min_value

print(min_value_linear(my_list))



# def min_square(my_list):
#     list_2 = my_list
#     while True:
#             if my_list[0] <= my_list[1]:
#                 list_2 = my_list.remove[1]
#             elif my_list[0] > my_list[1]:
#                 list_2 = my_list.remove[0]
#     # if my_list[0] <= my_list[1]:
#     #     return my_list[0]
#     # else:
#     #     return my_list[1]
#     return list_2

