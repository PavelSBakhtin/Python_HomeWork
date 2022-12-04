# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].

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
print(f"Original list: {a}")
x = l // 2
y = []
for i in range(x):
    y.append(a[i] * a[(l-1)-i])
if len(a) % 2 != 0:
    y.append(a[x]**2)
print(f"List multiplied: {y}")
