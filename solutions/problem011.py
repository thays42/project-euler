from problem5 import product

def transpose(lol):
    '''
    Returns the transpose of list of list input.
    Assumes list of list contains N lists, all of length N.
    '''
    return [[x[i] for x in lol] for i in range(len(lol))]


def main():
    '''
    In the 20×20 grid below, four numbers along a diagonal line have been marked
    in red.

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?

    '''

    # Go from a file to an integer list of lists
    with open("../inputs/problem11.txt", "rt") as f:
        grid = [[int(y) for y in x.strip().split(' ')] for x in f.readlines()]

    best, dim = 0, len(grid)
    # -
    for line in grid:
        for i in range(1, dim-3):
            best = max(best, product(line[i:i+3]))

    # |
    for line in transpose(grid):
        for i in range(1, dim-3):
            best = max(best, product(line[i:i+3]))

    # \
    for i, j in ((i, j) for i in range(dim - 3)
                        for j in range(dim - 3)):
        best = max(best, product(grid[i+k][j+k] for k in range(4)))

    # /
    for i, j in ((i, j) for i in range(3, dim - 1)
                        for j in range(dim - 3)):
        best = max(best, product(grid[i-k][j+k] for k in range(4)))

    print(best)

if __name__ == '__main__':
    main()
