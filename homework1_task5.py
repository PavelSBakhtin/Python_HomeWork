# Задача 5.
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

xA = int(input("Enter an integer for X at point A: "))
yA = int(input("Enter an integer for Y at point A: "))
xB = int(input("Enter an integer for X at point B: "))
yB = int(input("Enter an integer for Y at point B: "))

result = (((xA - xB) ** 2) + ((yA - yB) ** 2)) ** 0.5
print(f"Distance AB is: {format(result, '.2f')}")
