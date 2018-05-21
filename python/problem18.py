from problem8 import str_to_int_list

def read_triangle(filepath):
    with open(filepath, 'rt') as f:
        return [str_to_int_list(x.strip().split(' ')) for x in f.readlines()]

def main():
    '''
    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below: <file>
    '''

    triangle = read_triangle("../inputs/problem18.txt")

    for i in range(len(triangle)-1, 0, -1):
        for j in range(0, len(triangle[i]) - 1):
            triangle[i-1][j] = max(triangle[i][j], triangle[i][j+1]) + triangle[i-1][j]

    return triangle[0][0]

if __name__ == '__main__':
    print(main())
