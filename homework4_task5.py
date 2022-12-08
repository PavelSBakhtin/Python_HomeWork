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
