def collatz_function(n):
    '''
    Function for getting the next number in a Collatz sequence
    '''
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1

def collatz_sequence(n):
    '''
    Generator for a Collatz sequence
    '''
    while n != 1:
        yield n
        n = collatz_function(n)
    yield n
    return

def dynamic_collatz_length(n, history):
    '''
    Dynamic Collatz Length function that maintains a dictionary of
    previously found collatz sequence lengths to avoid duplicating work.
    '''
    if n in history:
        return history
    length, sequence = 1, [n]
    while n != 1:
        n = collatz_function(n)
        if n in history:
            length += history[n]
            break
        else:
            length += 1
            sequence.append(n)
    for i, number in enumerate(sequence):
        history[number] = length - i
    return history

def main():
    '''
    The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem), it
    is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    Once the chain starts the terms are allowed to go above one million.
    '''

    history = dict()
    for n in range(1, 10 ** 6):
        history = dynamic_collatz_length(n, history)

    return max(history.items(), key=lambda x: x[1])

if __name__ == '__main__':
    print(main())
