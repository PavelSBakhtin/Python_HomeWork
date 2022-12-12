# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = input()
count = 1
for i in range(len(text)-1):
    if i <= len(text):
        if text[i] == text[i + 1]:
            count += 1
        else:
            a = text[i]
            print(count, text[i])
            count = 1  
print(count, text[i])
