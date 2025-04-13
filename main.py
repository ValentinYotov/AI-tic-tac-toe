import random

# Празно поле
board = [' ' for _ in range(9)]

# Показване на полето
def print_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

# Ход на играч
def player_move_1():
    move = int(input("Избери позиция (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Невалиден ход!")
        player_move_1()

def player_move_2():
    move = int(input("Избери позиция (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'O'
    else:
        print("Невалиден ход!")
        player_move_1()

def check_winner(board, player):
    # Списък с всички печеливши комбинации (редове, колони, диагонали)
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # редове
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # колони
        [0, 4, 8], [2, 4, 6]              # диагонали
    ]
    
    # Проверяваме всяка комбинация
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            print(f"Играч {'1' if player == 'X' else '2'} печели!")
            return True
    return False
    
    

   
# Тест
for i in range(9):
    if i % 2 == 0:
        player_move_1()
    else:
        player_move_2()
    print_board()
    if check_winner(board, 'X'):
        break