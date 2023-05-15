import os

players = ["Player 1", "Player 2"]

def clearscreen():
    os.system('cls||clear')

def print_board(board):
    print(f"\t     |     |")
    print(f"\t  {board[0]}  |  {board[1]}  |  {board[2]}")
    print(f"\t_____|_____|_____")
    print(f"\t     |     |")
    print(f"\t  {board[3]}  |  {board[4]}  |  {board[5]}")
    print(f"\t_____|_____|_____")
    print(f"\t     |     |")
    print(f"\t  {board[6]}  |  {board[7]}  |  {board[8]}")
    print(f"\t     |     |")

# checking if input is valid, num1 and num2 are first and last items in menu
def menu_input_check(num1, num2):
    while True:
        try:
            user_choice = int(input())
            if num1 <= user_choice <= num2:
                break
            else:
                print(f"Please enter a valid input({num1}-{num2}): ", end = "")
                continue
        except ValueError:
            print(f"Please enter a valid input({num1}-{num2}): ", end = "")
            
    return user_choice
            
# checking if input is valid           
def player_move_check(player, occupied, players):
    if player == "X":
        print(f"It's {players[0]}'s turn. Your input(1-9): ", end = "")
    else: 
        print(f"It's {players[1]}'s turn. Your input(1-9): ", end = "") 
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
def player_move(player, occupied, round, board, players):
    # Checking if board position selected by player is valid
    player_choice = player_move_check(player, occupied, players)
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

def gameplay(players = ["X", "O"]):
    clearscreen()
    board_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Keeping track of the current player, already occupied spots on the board and round counter.
    current_player = "X"
    occupied_positions = []
    round_counter = 1
    while is_winner(board_positions) is False:
        clearscreen()
        print_board(board_positions)
        current_player, occupied_positions, round_counter, board_positions = player_move(current_player, occupied_positions, round_counter, board_positions, players)
        if round_counter == 10 and is_winner(board_positions) is False:
            clearscreen()
            print_board(board_positions)
            print(f"It's a draw!")
            with open("match_log.txt", "a") as match_log:
                match_log.write(f"&{players[0]} tied against {players[1]}.\n")
            with open("game_log.txt", "a") as game_log:
                for i in board_positions:
                    game_log.write(str(i))
                game_log.write("\n")
            break
        if is_winner(board_positions) is True:
            clearscreen()
            print_board(board_positions)
            if current_player == "X":
                print(f"The game is over. {players[1]} won.")
                with open("match_log.txt", "a") as match_log:
                    match_log.write(f"&{players[1]} won against {players[0]}.\n")
                with open("game_log.txt", "a") as game_log:
                    game_log.write("&")
                    for i in board_positions:
                        game_log.write(str(i))
                    game_log.write("\n")
            else: 
                print(f"The game is over. {players[0]} won.")
                with open("match_log.txt", "a") as match_log:
                    match_log.write(f"&{players[0]} won against {players[1]}.\n")
                with open("game_log.txt", "a") as game_log:
                    game_log.write("&")
                    for i in board_positions:
                        game_log.write(str(i))
                    game_log.write("\n")
            break
    
def menu():
    global players
    clearscreen()
    print("=========TIC TAC TOE=========")
    print(f"Welcome {players[0]} and {players[1]}!\n")
    print("  1) Play")
    print("  2) Enter player names")
    print("  3) View match history")
    print("  4) Exit\n")
    print("Choose from the menu(1-4): ", end = "")
    # checking if input is correct
    user_choice = menu_input_check(1, 4)
    if user_choice == 1:
        while True:
            gameplay(players)
            continue_playing_input = input("Would you like to play again? (y/n): ")
            if continue_playing_input.upper() != "Y":
                break
    elif user_choice == 2:
        players = player_names()
    elif user_choice == 3:
        while True:
            clearscreen()
            if print_match_history() < 5:
                clearscreen()
                print("You need to play at least 5 matches for Match History to initialize.")
                input("Press Any Button to return to menu")
                break
            print("\n  6) Back to menu\nYour input(1-6): ", end = "")
            match_history_input = menu_input_check(1, 6)
            if match_history_input == 6:
                break
            else: 
                clearscreen()
                print(f"Board state in game number {match_history_input}: \n\n")
                with open("game_log.txt") as game_log:
                    history_board_position = game_log.read()
                    history_board_position_split = history_board_position.split("&")
                    print_board(history_board_position_split[-match_history_input])
                print("  \n\n6) Back to menu")
                history_board_input = input("Your input: ")
                if history_board_input == "6":
                    break
    else: 
        exit
    
    return user_choice

def player_names():
    users = ["X", "O"]
    player1 = input("Player 1(X), enter your name: ")
    player2 = input("Player 2(O), enter your name: ")
    users[0] = player1
    users[1] = player2
    
    return users

def print_match_history():
    with open("match_log.txt", "r") as match_log:
        match_history = match_log.read()
        match_history_split = match_history.split("&")
        if len(match_history_split) < 5:
            print("You need to play at least 5 matches for Match History to initialize!\n")
        else: 
            for i in range(1, 6):
                print(f"{i}) {match_history_split[-i]}")
                
        return len(match_history_split)   
