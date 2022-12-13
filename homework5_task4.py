# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = input()
text = text + " "
count = 1
a = ''
for i in range(len(text)-1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        b = str(count)
        a = a + b
        a = a + text[i]
        count = 1
print(a)

def decoding(text):
    num = ''
    res = ''
    for i in range(len(text)):
        if text[i].isdigit():
            num += text[i]
        else:
            res = res + text[i] * int(num)
            num = ''
    return res
print(decoding(a))
