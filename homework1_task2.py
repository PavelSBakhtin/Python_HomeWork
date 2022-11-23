# Задача 2.
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2]) = not x[0] and not x[1] and not x[2])
# для всех значений предикат.

from random import randint

x = []
for i in range(3):
    x.append(randint(0, 2))
left = not (x[0] or x[1] or x[2])
right = not x[0] and not x[1] and not x[2]
print(left == right)
print(x[0], x[1], x[2])

# # Не моё решение, так - для коллекции:
# for x in range(3):
#     for y in range(3):
#         for z in range(3):
#             print(not (x or y or z) == (not x and not y and not z))
#             print(x, y, z)
