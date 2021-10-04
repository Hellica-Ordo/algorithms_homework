"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random

def guess_game(number, quess_count = 10):
    try:
        guess = int(input('Загадано число от 0 до 100. Угадаете?'))
        if guess == number:     # базовое условие
            print('Вы угадали!')
            return
        elif quess_count == 0:  # тоже базовое условие
            print(f"У вас закончились попытки. Загаданное число - {number}")
            return
        else:                   # шаг рекурсии
            if guess < number:
                print(f"Загаданное число больше. У вас осталось {quess_count} попыток.")
                return guess_game(number, quess_count - 1)
            if guess > number:
                print(f"Загаданное число меньше. У вас осталось {quess_count} попыток.")
                return guess_game(number, quess_count - 1)
    except ValueError:
        print(f"Вы ввели не число. У вас осталось {quess_count} попыток.")
        return guess_game(number, quess_count - 1)

print(guess_game(random.randint(0, 100)))