# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.

from random import randint
k = randint(2, 9)
print(f'Natural degree of k: {k}')
a = []
for i in range(k+1):
    a.append(randint(0, 100))
print(a)
b = []
for j in range(0, k+1):
    b.insert(0, j)
print(b)
c = []
for l in range(k-1):
    c.append(f'{a[l]}*x^{b[l]}')
c.append(f'{a[-2]}*x')
c.append(a[-1])
print(c)
d = ''
for h in range(k):
    d = d + (f'{c[h]} + ')
d =  d + (f'{c[-1]} = 0')
print(d)
with open('homework4_task4_f1.txt', 'a') as data:
    data.write(d + '\n')

# # Решение от преподавателя:
# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}')
#     flag = randint(0, 1)
#     ans.append(str(-1**flag))
#     k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()
