"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а


Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
"""
import hashlib

S = input('Пожалуйста, введите текст: ')
N = len(S)
unique = set()
for i in range(N):
    for j in range(i + 1, N + 1):
        if S[i:j] != S:
            unique.add(S[i:j])

hash_set = set()
for n in unique:
    hash_set.add(hashlib.sha256(n.encode()).hexdigest())

print(f'{S} - {len(hash_set)} уникальных подстрок.')