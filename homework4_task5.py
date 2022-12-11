# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def text_add(a, b):
    a = '-27*x^3 + 44*x^2 + 48*x + 54 = 0'
    with open('homework4_task5_f1.txt', 'w') as data:
        data.write(a)
    b = '66*x^3 + 33*x^2 + -22*x + 45 = 0'
    with open('homework4_task5_f2.txt', 'w') as data:
        data.write(b)
# text_add(0, 0)
def text_write(c):
    with open('homework4_task5_f3.txt', 'w') as data:
        data.write(c)
with open('homework4_task5_f1.txt', 'r') as data:
    for i in data:
        x = i
with open('homework4_task5_f2.txt', 'r') as data:
    for j in data:
        y = j
print(x)
print(y)
x = x.split(" + ")
#print(x)
lx = len(x)
for i in range(lx-2):
    x[i] = x[i][:-4]
x[-2] = x[-2][:-2]
x[-1] = x[-1][:-4]
for j in range(lx):
    x[j] = int(x[j])
# print(x)
y = y.split(" + ")
#print(y)
ly = len(y)
for i in range(ly-2):
    y[i] = y[i][:-4]
y[-2] = y[-2][:-2]
y[-1] = y[-1][:-4]
for j in range(ly):
    y[j] = int(y[j])
# print(y)
z = []
for h in range(lx):
    z.append(x[h] + y[h])
# print(z)
r = f"{z[0]}*x^3 + {z[1]}*x^2 + {z[2]}*x + {z[3]} = 0"
print(r)
text_write(r)

# # Интересное решение коллеги:
# def readpoly(poly):
#     poly = poly[:poly.find("=")]
#     poly = poly.split("+")
#     polynome1 = {}
#     for part in poly:
#         if part.count('^') == 1:
#             power = int(part[part.find('^') + 1:])
#             if part.count('*') == 1:
#                 const = int(part[:part.find('x') - 1])
#             else:
#                 const = 1

#         elif part.count('x') == 1:
#             power = 1
#             if part.count('*') == 1:
#                 const = int(part[:part.find('x') - 1])
#             else:
#                 const = 1
#         else:
#             power = 0
#             const = int(part)

#         polynome1[power] = const

#     return polynome1
# # ___________________________________
# def polynome_gen(dict_n):

#     polynome = '=0'

#     powers = sorted(dict_n.keys())
#     print(powers)

#     for pow_d in powers:
#         const = dict_n[pow_d]
#         if pow_d == 0:
#             polynome = "+" + str(const)+polynome
#         elif pow_d == 1:
#             if const == 1:
#                 polynome = "+x" + polynome
#             else:
#                 polynome = "+" + str(const) + "*x" + polynome
#         else:
#             if const == 1:
#                 polynome = "+x^" + str(pow_d) + polynome
#             else:
#                 polynome = "+" + str(const) + "*x^" + str(pow_d) + polynome

#     polynome = polynome[1:]

#     return polynome
# #    --------------------------------------------
# # path_1 = input("введите имя первого файла: ")
# # path_2 = input("введите имя второго файла: ")

# path_1 = "poly1"
# path_2 = "poly3"

# file = open(path_1, "r")
# poly1 = file.readline()
# file.close()

# file = open(path_2, "r")
# poly2 = file.readline()
# file.close()

# print(poly1, " ", poly2)

# poly_dic1 = readpoly(poly1)
# poly_dic2 = readpoly(poly2)

# print(poly_dic1, " ", poly_dic2)

# sum_dic = {}
# for k in poly_dic1.keys():

#     sum_dic[k] = poly_dic1[k] + poly_dic2.get(k, 0)
# # print(sum_dic)
# for k in poly_dic2.keys():
#     if poly_dic1.get(k, 0) == 0:
#         sum_dic[k] = poly_dic2[k]
# print(sum_dic)
# # sum_dic = dict(sorted(sum_dic.items(), reverse=True)) ??? не работает??? :(

# print(polynome_gen(sum_dic))
