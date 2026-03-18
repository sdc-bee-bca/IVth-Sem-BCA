"""
Tic Tac Toe

Statement: Create a simple command-line Tic Tac Toe game for two players. 
The game should allow players to take turns entering their positions, 
check for wins or draws, and display the game board after each move.
"""

# The game board is represented as a list of numbers from 1 to 9, 
# which correspond to the positions on the board.
board = [i for i in range(1, 10)]

# Initialize the board with numbers 1-9 representing positions
def print_board() -> None:
    """
    Print the current state of the game board.
    
    Args:
        None
    
    Returns:
        None
    """
    print('-------------')
    for i in range(3):
        print(f'| {board[0 + i*3]} | {board[1 + i*3]} | {board[2 + i*3]} |')
        print('-------------')


def check_winner() -> bool:
    """
    Check if there is a winner in the current game state.

    Args:
        None
        
    Returns:
        bool: True if there is a winner, False otherwise
    """ 
    # Define winning combinations (rows, columns, diagonals)
    win_com = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]
    # Check if any winning combination has the same symbol (either 'X' or 'O')
    for a, b, c in win_com:
        if board[a] == board[b] == board[c]:
            return True
    return False


def check_draw() -> bool:
    """
    Check if the game is a draw.

    Args:
        None

    Returns:
        bool: True if the game is a draw, False otherwise
    """
    # Check if all positions are taken (i.e., all are strings 'X' or 'O')
    return all(isinstance(data, str) for data in board)
    # for data in board:
    #     if data not in ['X', 'O']:
    #         return False
    # return True


def start_game(player_1: str, player_2: str) -> None:
    """
    Start the Tic Tac Toe game.

    Args:
        player_1 (str): Name of the first player.
        player_2 (str): Name of the second player.

    Returns:
        None
    """
    # Set the current player to player_1 and print the initial game board
    current_player = player_1
    print_board()

    # Main game loop: continue until there is a winner or a draw
    while True:
        # Prompt the current player to enter their position (1-9) and adjust for 0-based indexing
        pos = int(input(f'{current_player}, please enter your position (1-9): '))
        pos -= 1  
        
        # Validate the input position: check if it's within the valid range and not already taken
        if pos < 0 or pos > 8:
            print('invalid position. please enter a number between 1 and 9.')
            continue
        
        if board[pos] in ['X', 'O']:
            print('This spot is already taken. please try again.')
            continue
        
        # Update the board with the current player's symbol ('X' for player_1 and 'O' for player_2) and print the updated board
        board[pos] = 'X' if current_player == player_1 else 'O'
        print_board()
        
        # Check for a winner after the current move. If there is a winner, congratulate the player and break the loop
        if check_winner():
            print(f'Congratulations {current_player}, you win!')
            break

        # Check for a draw after the current move. If the game is a draw, announce the result and break the loop
        if check_draw():
            print('The game is a draw!')
            break

        # Switch the current player for the next turn
        current_player = player_2 if current_player == player_1 else player_1


def main() -> None:
    """
    Main function to start the Tic Tac Toe game.
    
    Args:
        None
        
    Returns:
        None
    """
    print('Welcome to Tic Tac Toe!')

    player_1 = input('Player 1, please enter your name: ')
    player_2 = input('Player 2, please enter your name: ')

    print(f'{player_1} will be X and {player_2} will be O.')
    
    start_game(player_1, player_2)


if __name__ == '__main__':
    main()