# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример: Для n=4 {1:2, 2:2.25, 3:2.37, 4:2.44} -> Сумма = 9.06

a = int(input("Enter any integer: "))
b = {i: round((1 + 1 / i) ** i, 2) for i in range(1, a + 1)} 
print(b)
c = 0
for i in range(1, a + 1):
    c += b[i]
print(c)

# # Решение от преподавателя:
# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += (1 + 1 / i) ** i
# print(summ)
