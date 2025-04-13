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
def player_move():
    move = int(input("Избери позиция (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Невалиден ход!")
        player_move()

# Случаен ход за AI
def ai_move():
    free_spots = [i for i in range(9) if board[i] == ' ']
    move = random.choice(free_spots)
    print(f"AI предлага ход: {move + 1}")
    board[move] = 'O'

# Тест
print_board()
player_move()
ai_move()
print_board()