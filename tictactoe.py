import sys

# The game board is a list of 9 strings, initially representing empty spaces or guiding player input
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
current_player = "X"
winner = None
game_running = True

def display_board():
    """Prints the current state of the board in a 3x3 grid format."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def get_player_input():
    """Prompts the player to enter a number from 1-9 and validates the move."""
    while True:
        move = input(f"Player {current_player}, enter a cell number (1-9): ")
        try:
            move = int(move) - 1 # Convert to 0-indexed list position
            if 0 <= move <= 8:
                if board[move] in ["X", "O"]:
                    print("Oops, that spot is already taken. Try again.")
                    continue
                else:
                    board[move] = current_player
                    break
            else:
                print("The number must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win():
    """Checks all possible winning combinations (rows, columns, diagonals)."""
    global winner
    # Define winning combinations
    winning_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] in ["X", "O"]:
            winner = board[combo[0]]
            return True
    return False

def check_tie():
    """Checks if the board is full without a winner."""
    global game_running
    if all(cell in ["X", "O"] for cell in board):
        display_board()
        print("Game ends in a draw.")
        game_running = False
        return True
    return False

def switch_player():
    """Switches the turn to the other player."""
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Main game loop
print("Welcome to Tic-Tac-Toe!")
while game_running:
    display_board()
    get_player_input()
    if check_win():
        display_board()
        print(f"Player {winner} has won! Hooray!")
        game_running = False
    elif check_tie():
        pass # Message already printed in check_tie()
    else:
        switch_player()

