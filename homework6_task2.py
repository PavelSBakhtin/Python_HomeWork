# Предложить улучшения кода, для уже решённых задач, с использованием:
# lambda, filter, map, zip, enumerate, list comprehension.
# hw3t5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k=8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# list comprehension
import random
a = random.randint(5, 11)
b = [1, 1]
[b.append(b[i-2] + b[i-1]) for i in range(2, a)]
[b.insert(0, b[1] - b[0]) for i in range(a + 1)]
print(b)

# numbers = [2, 3, 4, 5, 6, 7, 5, 4]
# diff = [a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])]
# print(diff)

# t=[x*y for x, y in zip(s[-1:int(round(len(s)/2+0.1))-2:-1], s[0:int(round(len(s)/2+0.1)):1])]
# print(t)

# import random
# a = random.randint(5, 11)
# b = [1, 1]
# [b.append(b[i-2] + b[i-1]) for i in range(2, a)] + [b.insert(0, b[1] - b[0]) for i in range(a + 1)]
# print(b)
