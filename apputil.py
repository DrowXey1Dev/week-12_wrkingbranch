import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    """
    Perform the step of conway's game of life on a binary numpy array

    Function parameters:
    current_board : numpy.ndarray (a 2D binary array (elements 0 or 1) representing the current board state)

    Function returns:
    numpy.ndarray (the updated board after applying one iteration of Conway's rules)
    """
    #copy board before updating
    board = current_board.copy()
    rows, cols = board.shape

    #create new board to fill
    new_board = np.zeros((rows, cols), dtype=int)

    #count the neighbors using convolution logic
    for r in range(rows):
        for c in range(cols):

            #define 8 neighborhood coordinates
            neighbors = [
                (r-1, c-1), (r-1, c), (r-1, c+1),
                (r,   c-1),           (r,   c+1),
                (r+1, c-1), (r+1, c), (r+1, c+1)
            ]

            #count active neighbors
            active_neighbors = 0
            for x, y in neighbors:
                if 0 <= x < rows and 0 <= y < cols:
                    active_neighbors += board[x, y]

            cell = board[r, c]

            #apply conways rules:
            if cell == 1:
                #recall that rule 1 and 3: survives with 2 or 3 neighbors
                if active_neighbors in (2, 3):
                    new_board[r, c] = 1
            else:
                #recall also that rule 4: reproduction with exactly 3 neighbors
                if active_neighbors == 3:
                    new_board[r, c] = 1

    #prep to pass out the board based off of the existing program sturcture
    current_board = new_board
    updated_board = current_board

    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)