# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101, 3 -> 11, 2 -> 10.

import random
a = random.randint(0, 100)
b = a
# print(a)
# print(bin(a))
c = ""
while b > 0:
    c = str(b % 2) + c
    b = b // 2
print(f"{a} -> {c}")
