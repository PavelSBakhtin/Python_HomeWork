# Задача 1.
# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

x = int(input("Enter the number of the day of the week: "))
if x < 8 and x > 0:
    if x < 6:
        print("No, it's not a weekday!")
    else:
        print("Yes, it's a weekday!")
else:
    print("There is no such day of the week!")

# x = int(input("Enter the number of the day of the week: "))
# if x < 8 and x > 0:
#     if x == 1: print("Monday")
#     if x == 2: print("Tuesday")
#     if x == 3: print("Wednesday")
#     if x == 4: print("Thursday")
#     if x == 5: print("Friday")
#     if x == 6: print("Saturday")
#     if x == 7: print("Sunday")
# else:
#     print("There is no such day of the week!")
