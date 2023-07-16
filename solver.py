
"""
Checks whether a number can be placed at a specified board position.

Parameters:
    board (ndarray): the current sudoku game state.
    row (int): the row index of the specified position.
    col (int): the column index of the specified position.
    num (int): the number to be placed at the specified position
    
Returns:
    bool: whether or not the number can be placed at the specified position.
"""
    
def is_valid(board, row: int, col: int, num: int):
    for i in range(9):
        if board.matrix[i][col] == num:
            return False

        if board.matrix[row][i] == num:
            return False

        if board.matrix[3 * (row//3) + i//3][3 * (col//3) + i % 3] == num:
            return False

    return True


"""
Finds a solution to a sudoku board using recursive backtracking.
Modifies the board in place and returns if solution is found.

Parameters:
    board(ndarray): the current sudoku game state.
Returns:
    bool: whether the sudoku has been solved or not.
"""


def solve_board(board):
    def solve(row, col):
        if row == 9:
            return True
        if col == 9:
            return solve(row + 1, 0)
        if board.board[row][col] == '.':
            for i in range(1, 10):
                if board.is_valid(row, col, str(i)):
                    board.board[row][col] = str(i)
                    if solve(row, col + 1):
                        return True
                    else:
                        board.board[row][col] = "."
            return False
        else:
            return solve(row, col + 1)
        
    solve(0, 0)


