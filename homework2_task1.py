# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 6782 -> 23, 0,56 -> 11.

def sum(num):
    s = 0
    for i in str(num):
        if i != ".":
            s += int(i)
    return s

n = input("Enter any number: ")
print(f"Sum of digits: {sum(n)}")

# # Решение от преподавателя:
# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))
