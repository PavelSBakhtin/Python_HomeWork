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
