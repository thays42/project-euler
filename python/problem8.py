from problem5 import product


def str_to_int_list(s):
    '''
    Transform a string of integers into a list of digits
    '''
    return [int(x) for x in s]


def main():
    '''
    Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product. What is the value of this product?
    '''
    with open('../inputs/problem8.txt', 'rt') as f:
        numbers = str_to_int_list(f.read().replace('\n', ''))

    return max([product(numbers[i:i+13])
                for i in range(len(numbers) - 13 + 1)
                if 0 not in numbers[i:i+13]])


if __name__ == '__main__':
    print(main())
