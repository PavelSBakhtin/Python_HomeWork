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
