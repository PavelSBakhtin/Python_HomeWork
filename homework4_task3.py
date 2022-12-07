# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

a = randint(5, 10)
b = []
for i in range(a):
    b.append(randint(1, 9))
print(b)
c = []
for i in b:
    if b.count(i) == 1:
        c.append(i)
print(c)
