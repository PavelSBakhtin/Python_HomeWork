# Реализуйте алгоритм перемешивания списка.

import random
l = random.randint(6, 9)
a = []
for i in range(l):
    k = random.randint(97, 121)
    r = chr(k)
    # print(r)
    if r in a:
        r = chr(k + 1)
        a.append(r)
    else:
        a.append(r)
print(a)
a[0], a[l - 3] = a[l - 3], a[0]
a[1], a[l - 2] = a[l - 2], a[1]
a[2], a[l - 1] = a[l - 1], a[2]
print(a)

# # Решение от преподавателя:
# import random
# list = ["Anna", "Alex", 0, 3.14159]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     temp = list[i]
#     list[i] = list[index_a]
#     list[index_a] = temp
# print(list)
