# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
a = []
l = random.randint(5, 9)
for i in range(l):
    k = random.randint(1, 9)
    r = k
    if r in a:
        r += 10
        a.append(r)
    else:
        a.append(k)
print(a)
# a = [2, 3, 5, 9, 3]
b = []
s = 0
for i in range(len(a)):
    if i % 2 != 0:
        b.append(a[i])
# for i in range(1, len(a), 2):
#     b.append(a[i])
print(b)
for j in b:
    s += j
print(f"Sum of numbers in odd positions: {s}")
