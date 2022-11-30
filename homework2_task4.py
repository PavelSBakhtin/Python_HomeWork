# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на рандомных позициях.

n = int(input("Enter any integer: "))
x = []
for i in range(-n, n + 1):
    x.append(i)
print(f"[-N, N]: {x}")
y = len(x)
print(f"List length: {y}")
import random
l = random.randint(2, 4) # количество элементов для их произведения
print(f"Number of elements to multiply: {l}")
a = [] # список элементов для их произведения
for i in range(l):
    r = random.randrange(x[0], x[y - 2], 1)
    if r != 0:
        a.append(r)
    else:
        a.append(x[y - 1])
print(f"Elements for multiples: {a}")
s = 1; k = 0
while k < len(a):
    s *= a[k]
    k += 1
print(f"Multiplication is: {s}")
