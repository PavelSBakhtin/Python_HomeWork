# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: Для N = 4: [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4).

def factor(n):
    if n != 1:
        return n * factor(n - 1)
    else:
        return 1

a = int(input("Enter any integer: "))
b = []
for i in range(1, a + 1):
    b.append(factor(i))
print(b)
