"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile

your_number = input('Введите целое число: ')

@profile
def wrapper():
    def inside_out(your_number, number_reversed =''):
        if your_number == 0:
            return number_reversed
        else:
            number_reversed += str(int(your_number) % 10)
            your_number = int(your_number) // 10
            return inside_out(your_number, number_reversed)
    return inside_out(your_number, number_reversed='')

print(wrapper())

"""ВЫВОДЫ:
Для того, чтобы корректно профилировать рекурсивную функцию, необходимо поместить её в тело другой функции, и профилировать именно функцию-обёртку."""
