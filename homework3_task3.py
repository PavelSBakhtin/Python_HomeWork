# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
a = []
l = 5
# l = random.randint(5, 9)
for i in range(l):
    k = round(random.uniform(1.0, 10.5), 2)
    a.append(k)
print(f"Original list: {a}")
b = []
for i in range(l):
    k = a[i] - (a[i] // 1)
    b.append(round(k, 2))
# print(f"List of shares: {b}")
if min(b) == 0:
    b.remove(0)
# print(f"List without null: {b}")
print(f"The difference max - min = {max(b) - min(b)}")
