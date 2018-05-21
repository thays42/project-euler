def name_score(name):
    return sum(ord(letter) - 64 for letter in name)


def main():
    '''
    Using names.txt a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical
    position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
    would obtain a score of 938 * 53 = 49714.

    What is the total of all the name scores in the file?
    '''
    with open('../inputs/problem22.txt', 'rt') as f:
        names = sorted(f.readline().replace('"', '').split(','))

    return sum(name_score(name) * (index + 1) for index, name in enumerate(names))

if __name__ == '__main__':
    print(main())
