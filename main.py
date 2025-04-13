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

# Ход на играч 1 (човек)
def player_move_1():
    try:
        move = int(input("Избери позиция (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == ' ':
            board[move] = 'X'
        else:
            print("Невалиден ход! Опитай пак.")
            player_move_1()
    except (ValueError, IndexError):
        print("Моля, въведи число между 1 и 9!")
        player_move_1()

# Проверка за победител
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # редове
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # колони
        [0, 4, 8], [2, 4, 6]              # диагонали
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Проверка за равенство
def check_draw():
    return ' ' not in board

# Minimax алгоритъм
def minimax(board, is_maximizing):
    # Проверка за край на играта
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # Пробва ход за AI
                score = minimax(board, False)
                board[i] = ' '  # Връща хода обратно
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Пробва ход за играча
                score = minimax(board, True)
                board[i] = ' '  # Връща хода обратно
                best_score = min(score, best_score)
        return best_score

# Ход на AI с Minimax
def ai_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        print(f"AI избира позиция: {best_move + 1}")
        board[best_move] = 'O'

# Основна игра
while True:
    print_board()
    player_move_1()
    if check_winner(board, 'X'):
        print_board()
        print("Играч 1 печели!")
        break
    if check_draw():
        print_board()
        print("Равенство!")
        break
    ai_move()
    if check_winner(board, 'O'):
        print_board()
        print("AI печели!")
        break
    if check_draw():
        print_board()
        print("Равенство!")
        break