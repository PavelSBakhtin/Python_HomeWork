# Задача 4.
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

z = int(input("Enter the quarter plane: "))

if z == 1:
    print("Range of possible coordinates of points in this quarter: x > 0, y > 0")
elif z == 2:
    print("Range of possible coordinates of points in this quarter: x < 0, y > 0")
elif z == 3:
    print("Range of possible coordinates of points in this quarter: x < 0, y < 0")
elif z == 4:
    print("Range of possible coordinates of points in this quarter: x > 0, y < 0")
else:
    print("Incorrect quarter plane value entered")
