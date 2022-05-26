# solver.py

# 1. pick empty, find_empty function
# 2. try  numbers until step 3
# 3. find one that works, valid function
# 4. repeat
# 5. backtrack when it doesn't work, valid/solve function

# The actual backtracking function is here, works in 5 steps:
def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """

    find = find_empty(bo)
    if not find:
        # soduku has been solved
        return True
    else:
        row, col = find

    for i in range(1,10):
        # Checks to see if adding values 1-9 in the board will make valid solution
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # recursively calls the function again
            if solve(bo):
                return True

            # reset last element to zero
            bo[row][col] = 0

    return False


# This function determine whether every given position on the sodoku board
# follows the rules of the game
def valid(bo, num, pos):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """
    # Check row
    for i in range(len(bo[0])):
        # pos is a tuple, the (i, j) that gets returned by the find_empty function
        # Checks if each number in a row is equal to the number just placed, and
        # skips over the number in the row that was just placed through 'pos[1] != i'
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    # There are 9 boxes, the top left box is (0,0) and the bottom right
    # box is (3, 3), with respect to (box_x, box_y)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Using what box you're in, these two loops permit you to
    # get through the relevant indexes for this function's purpose
    # to validate/invalidate a given soduku board
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            # makes sure to check no duplicates, while skipping over the actual position
            # that is currently being checked
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                # the 'end=""' just prevents a new line from being formed after this print statement
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# Looks for empty spaces on the whole board, returns a tuple with the row and column coordinates
def find_empty(bo):
    """
    finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    #return none when there are no more squares to solve
    return None
