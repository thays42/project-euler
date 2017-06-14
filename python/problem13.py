def main():
    '''
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.
    '''

    with open("../inputs/problem13.txt", "rt") as f:
        return str(sum([int(x.strip()) for x in f.readlines()]))[:10]

if __name__ == '__main__':
    print(main())
