import random
import os

def print_board(board):
    print("\n")
    print(f"\t     |     |")
    print(f"\t  {board[0]}  |  {board[1]}  |  {board[2]}")
    print(f"\t_____|_____|_____")
    print(f"\t     |     |")
    print(f"\t  {board[3]}  |  {board[4]}  |  {board[5]}")
    print(f"\t_____|_____|_____")
    print(f"\t     |     |")
    print(f"\t  {board[6]}  |  {board[7]}  |  {board[8]}")
    print(f"\t     |     |")
    print(f"\n")
    
def menu():
    print("Welcome to Tic-Tac-Toe!\n")
    print("  1) Play")
    print("  2) View match history")
    print("  3) Exit")

# checking if input is valid
def player_move_check(player, occupied):
    print(f"It's {player}'s turn. Make your turn(1-9): ", end = "")
    player_choice = 0
    while True:
        try:
            player_choice = int(input())
            if 0 < player_choice < 10 and player_choice not in occupied:
                break
            else:
                print("Please enter a valid move(1-9): ", end = "")
                continue
        except ValueError:
            print("Please enter a valid move(1-9): ", end = "")
    
    return player_choice

# updating board with player move
def player_move(player, occupied, round, board):
    player_choice = player_move_check(player, occupied)
    occupied.append(player_choice)
    # updating board and swapping current player
    board[player_choice-1] = player
    player = "O" if player == "X" else "X"
    round += 1
    return player, occupied, round, board

# checking all 8 winning board positions
def is_winner(board):
    for i in range(0,9,3):
        if board[i] == board[i+1] and board[i] == board[i+2]:
            return True
    for i in range(0,3):
        if board[i] == board[i+3] and board[i] == board[i+6]:
            return True
    if (board[0] == board[4] and board[0] == board[8]) or (board[2] == board[4] and board[2] == board[6]):
        return True
    
    return False

def gameplay():
    os.system('cls||clear')
    board_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_player = "X"
    occupied_positions = []
    round_counter = 1
    while is_winner(board_positions) is False:
        os.system('cls||clear')
        print_board(board_positions)
        current_player, occupied_positions, round_counter, board_positions = player_move(current_player, occupied_positions, round_counter, board_positions)
        if round_counter == 10 and is_winner(board_positions) is False:
            os.system('cls||clear')
            print_board(board_positions)
            print(f"It's a draw!")
            break
        if is_winner(board_positions) is True:
            os.system('cls||clear')
            print_board(board_positions)
            if current_player is "X":
                print(f"The game is over. O won.")
            else: 
                print(f"The game is over. X won.")
            break