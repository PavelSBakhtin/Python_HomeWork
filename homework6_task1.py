# Предложить улучшения кода, для уже решённых задач, с использованием:
# lambda, filter, map, zip, enumerate, list comprehension.
# hw2t1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 6782 -> 23, 0,56 -> 11.

n = abs(float(input("Enter any number: ")))
if n % 1 != 0:
    x = len(str(float(n))[str(float(n)).index('.')+1:])
    while x > 0:
        n = round(n * 10, x)
        x -= 1
n = str(int(n))
print(sum(map(int, n)))
