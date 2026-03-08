# Tic Tac Toe

# Statement: Create a simple command-line Tic Tac Toe game for two players. 
# The game should allow players to take turns entering their positions, 
# check for wins or draws, and display the game board after each move.


# Initialize the board with numbers 1-9 representing positions
board = [i for i in range(1, 10)]

def print_board():
    # Print the current state of the board
    print('-------------')
    for i in range(3):
        print(f'| {board[0 + i*3]} | {board[1 + i*3]} | {board[2 + i*3]} |')
        print('-------------')

def check_winner():
    # Define winning combinations (rows, columns, diagonals)
    win_com = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    # Check if any winning combination has the same symbol (either 'X' or 'O')
    for a, b, c in win_com:
        if board[a] == board[b] == board[c]:
            return True
    return False


def check_draw():
    # Check if all positions are taken (i.e., all are strings 'X' or 'O')
    return all(isinstance(data, str) for data in board)


def start_game(player_1, player_2):
    # Set the current player to player_1 (X starts first)
    current_player = player_1
    print_board()

    
    # Start the game loop
    while True:
        # Get the position from the current player
        pos = int(input(f'{current_player}, please enter your position (1-9): '))
        pos -= 1  # Adjust for 0-based index
        
        # Validate the input
        # # if pos < 0 or pos > 8:
        # #     print('invalid position. please enter a number between 1 and 9.')
        # #     continue
        # # if board[pos] in ['X', 'O']:  # (OR) if board[pos] == 'X' or board[pos] == 'O':
        # #     print('This spot is already taken. please try again.')
        # #     continue
        
        # Update the board with the current player's symbol
        board[pos] = 'X' if current_player == player_1 else 'O'
        print_board()
        
        # Check for a winner or a draw after each move
        if check_winner():
            print(f'Congratulations {current_player}, you win!')
            break

        if check_draw():
            print('The game is a draw!')
            break

        # Switch the current player for the next turn
        current_player = player_2 if current_player == player_1 else player_1


def main():
    # Welcome message
    print('Welcome to Tic Tac Toe!')

    # Get player names
    player_1 = input('Player 1, please enter your name: ')
    player_2 = input('Player 2, please enter your name: ')

    print(f'{player_1} will be X and {player_2} will be O.')
    
    # Start the game
    start_game(player_1, player_2)


# Run the main function to prepare for the game
if __name__ == '__main__':
    main()



# OUTPUT 1:

# Welcome to Tic Tac Toe!
# Player 1, please enter your name: Bee
# Player 2, please enter your name: Prince
# Bee will be X and Prince will be O.
# -------------
# | 1 | 2 | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Bee, please enter your position (1-9): 1
# -------------
# | X | 2 | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Prince, please enter your position (1-9): 2
# -------------
# | X | O | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Bee, please enter your position (1-9): 5
# -------------
# | X | O | 3 |
# -------------
# | 4 | X | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Prince, please enter your position (1-9): 4
# -------------
# | X | O | 3 |
# -------------
# | O | X | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Bee, please enter your position (1-9): 9
# -------------
# | X | O | 3 |
# -------------
# | O | X | 6 |
# -------------
# | 7 | 8 | X |
# -------------
# Congratulations Bee, you win!



# OUTPUT 2:

# Welcome to Tic Tac Toe!
# Player 1, please enter your name: Bee
# Player 2, please enter your name: Prince
# Bee will be X and Prince will be O.
# -------------
# | 1 | 2 | 3 |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Bee, please enter your position (1-9): 3
# -------------
# | 1 | 2 | X |
# -------------
# | 4 | 5 | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# Prince, please enter your position (1-9): 7
# -------------
# | 1 | 2 | X |
# -------------
# | 4 | 5 | 6 |
# -------------
# | O | 8 | 9 |
# -------------
# Bee, please enter your position (1-9): 6
# -------------
# | 1 | 2 | X |
# -------------
# | 4 | 5 | X |
# -------------
# | O | 8 | 9 |
# -------------
# Prince, please enter your position (1-9): 3
# This spot is already taken. please try again.
# Prince, please enter your position (1-9): 4
# -------------
# | 1 | 2 | X |
# -------------
# | O | 5 | X |
# -------------
# | O | 8 | 9 |
# -------------
# Bee, please enter your position (1-9): 0
# Invalid position. please enter a number between 1 and 9.
# Bee, please enter your position (1-9): 9
# -------------
# | 1 | 2 | X |
# -------------
# | O | 5 | X |
# -------------
# | O | 8 | X |
# -------------
# Congratulations Bee, you win!