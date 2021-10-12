"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
import timeit
from cProfile import run

def revers_1(enter_num, revers_num=0):      # рекурсия
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):      # цикл
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):                    # срез
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_suggestion(enter_num):           # методы join + reverse
    return int(''.join(reversed(str(enter_num))))

enter_num = int(input('Пожалуйста, введите целое число: '))

print(timeit.timeit("revers_1(enter_num)", globals = globals(), number = 150000))
print(timeit.timeit("revers_2(enter_num)", globals = globals(), number = 150000))
print(timeit.timeit("revers_3(enter_num)", globals = globals(), number = 150000))
print(timeit.timeit("revers_suggestion(enter_num)", globals = globals(), number = 150000))

run('revers_1(150000)')
run('revers_2(150000)')
run('revers_3(150000)')
run('revers_suggestion(150000)')

"""
ВЫВОДЫ:
Функции имеют разную эффективность:
revers_1 - самая медленная, наибольшая сложность О. Если бы мы добавили мемоизацию через декоратор, это бы повысило её скорость, но такое решение
всё равно не стало бы наиболее оптимальным.
revers_2 - предпоследняя по скорости выполнения, сложность О меньше, чем у рекурсии.
revers_3 - наиболее эффективная функция для данной задачи. В ней наименьшее количество операций и сложность О.
revers_suggestion - вторая по скорости выполнения, но заметно медленнее функции revers_3. Это связано с тем, что в ней используются два метода,
которые хоть и быстрее цикла или рекурсии, но всё равно не так оптимальны. 
"""