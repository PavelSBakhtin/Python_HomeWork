# Задача 3.
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.

x = float(input("Enter X value not equal to 0: "))
y = float(input("Enter Y value not equal to 0: "))

while x == 0 or y == 0:
    print("X and Y values must not be null")
    break

if x > 0 and y > 0:
    print("The point is in a quarter plane: 1")

if x < 0 and y > 0:
    print("The point is in a quarter plane: 2")

if x < 0 and y < 0:
    print("The point is in a quarter plane: 3")

if x > 0 and y < 0:
    print("The point is in a quarter plane: 4")
