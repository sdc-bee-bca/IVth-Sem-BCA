# Tic Tac Toe

# Statement: Create a simple command-line Tic Tac Toe game for two players. 
# The game should allow players to take turns entering their positions, 
# check for wins or draws, and display the game board after each move.

board = [i for i in range(1, 10)]


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
    win_com = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]
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
    current_player = player_1
    print_board()

    while True:
        pos = int(input(f'{current_player}, please enter your position (1-9): '))
        pos -= 1  
        
        if pos < 0 or pos > 8:
            print('invalid position. please enter a number between 1 and 9.')
            continue
        
        if board[pos] in ['X', 'O']:
            print('This spot is already taken. please try again.')
            continue
        
        board[pos] = 'X' if current_player == player_1 else 'O'
        print_board()
        
        if check_winner():
            print(f'Congratulations {current_player}, you win!')
            break

        if check_draw():
            print('The game is a draw!')
            break

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