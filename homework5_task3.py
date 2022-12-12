# Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))

def game_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("¯" * 13)

def place_input(player):
    check_place = False
    while not check_place:
        player_place = int(input(f"Choose place {player}: "))
        if player_place >= 1 and player_place <= 9:
            if(str(board[player_place - 1]) not in "XO"):
                board[player_place - 1] = player
                check_place = True
            else:
                print("This place is already taken")
        else:
            print("Invalid input. Choose place from 1 to 9.")

def check_game(board):
    win_plan = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_plan:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    count = 0
    victory = False
    while not victory:
        game_board(board)
        if count % 2 == 0:
           place_input("X")
        else:
           place_input("O")
        count += 1
        if count > 4:
           who = check_game(board)
           if who:
              print(who, "Won")
              victory = True
              break
        if count == 9:
            print("Standoff")
            break
    game_board(board)

game(board)

input("Press Enter to exit")
