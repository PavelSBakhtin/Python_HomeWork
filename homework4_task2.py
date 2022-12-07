# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

a = int(input("Enter any integer: "))
if a <= 1:
    print("Try again and enter a positive natural integer")
    exit()
b = []
c = 2
while c * c <= a:
    if a % c == 0:
        b.append(c)
        a //= c
    else:
        c += 1
if a > 1:
    b.append(a)
print(b)

# # Так, для себя интересный момент:
# b = []
# c = 2
# i = 0
# d = [i]
# while c * c <= a:
#     if a % c == 0:
#         b.append(c)
#         d[i] += 1
#         a //= c
#     else:
#         c += 1
#         i += 1
#         d.append(0)
# if a > 1 and a == b[-1]:
#     b.append(a)
#     d[-1] += 1
# elif a > 1:
#     b.append(a)
#     d.append(1)
# while 0 in d:
#     d.remove(0)
# print(b)
# print(d)
