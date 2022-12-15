# Предложить улучшения кода, для уже решённых задач, с использованием:
# lambda, filter, map, zip, enumerate, list comprehension.
# hw4t3
# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
a = randint(5, 10)
b = []
for i in range(a):
    b.append(randint(1, 9))
print(b)
c = filter(lambda i: b.count(i) == 1, b)
print(c)
