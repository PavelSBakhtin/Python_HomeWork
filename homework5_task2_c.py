# Создайте программу для игры с конфетами человек против "искусственного интеллекта".
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

import random
sweets_table = int(input("Enter the sum of sweets: "))  # вводится вручную
# sweets_table = random.randint(57, 2021) # задаётся рандомно
# print(f"The sum of sweets on table: {sweets_table}") # количество конфет на столе
first_player = input("Enter your name: ")
second_player = "Bot AI"
first_count = 0
second_count = 0
turn = random.randint(1, 2)  # жеребьёвка
if turn == 1:
    print(f"First turn: {first_player}")
else:
    print(f"First turn: {second_player}")

def input_value(player):
    x = int(input(f"{player}, enter sun of sweets to take from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{player}, enter sun of sweets to take from 1 to 28: "))
    return x

def result(player, k, count, sweets):
    print(
        f"Went down {player}, he took {k}, now he has {count}. Now on the table {sweets} sweets.")

def turn_ai(sweets, count1, count2):
    if count1 == 0 and count2 == 0:
        if sweets % 28 == 1:
            k = 1
        else:
            k = sweets % 28 - 1
    elif 29 < sweets < 57:
        k = sweets - 29
    elif sweets < 29:
        k = sweets
    else:
        if sweets % 28 == 0:
            k = 27
        elif sweets % 28 == 1:
            k = 28
        else:
            k = sweets % 28 - 1
    return k

while sweets_table > 0:
    if turn == 1:
        k = input_value(first_player)
        first_count += k
        sweets_table -= k
        turn = 2
        result(first_player, k, first_count, sweets_table)
        continue
    else:
        k = turn_ai(sweets_table, first_count, second_count)
        second_count += k
        sweets_table -= k
        turn = 1
        result(second_player, k, second_count, sweets_table)
        continue

if turn == 2:
    print(f"The player {first_player} won")
else:
    print(f"The player {second_player} won")
