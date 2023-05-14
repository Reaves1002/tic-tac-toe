import random
board_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"
occupied_positions = [3]

def print_board():
    print("\n")
    print(f"\t     |     |")
    print(f"\t  {board_positions[0]}  |  {board_positions[1]}  |  {board_positions[2]}")
    print(f"\t_____|_____|_____")
    print(f"\t     |     |")
    print(f"\t  {board_positions[3]}  |  {board_positions[4]}  |  {board_positions[5]}")
    print(f"\t_____|_____|_____")
    print(f"\t     |     |")
    print(f"\t  {board_positions[6]}  |  {board_positions[7]}  |  {board_positions[8]}")
    print(f"\t     |     |")
    print(f"\n")
    
def menu():
    print("Welcome to Tic-Tac-Toe!\n")
    print("  1) Play")
    print("  2) View match history")
    print("  3) Exit")

# making sure player move is valid(1-9) and not occupied + updating board
def player_move():
    global current_player
    print(f"It's {current_player}'s turn. Make your turn(1-9): ", end = "")
    player_choice = 0
    while True:
        try:
            player_choice = int(input())
            if 0 < player_choice < 10 and player_choice not in occupied_positions:
                break
            else:
                print("Please enter a valid move(1-9): ", end = "")
                continue
        except ValueError:
            print("Please enter a valid move(1-9): ", end = "")
    occupied_positions.append(player_choice)
    # updating board and swapping current player
    board_positions[player_choice-1] = current_player
    current_player = "O" if current_player == "X" else "X"

# checking all 8 winning board positions
def is_winner(board):
    for i in range(0,10,4):
        if board[i] == board[i+1] and board[i] == board[i+2]:
            return True
    for i in range(0,3):
        if board[i] == board[i+3] and board[i] == board[i+6]:
            return True
    if (board[0] == board[4] and board[0] == board[8]) or (board[2] == board[4] and board[2] == board[6]):
        return True
    
    return False

