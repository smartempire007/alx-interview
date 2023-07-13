#!/usr/bin/env python3
'''In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0'''


def minOperations(n):
    '''calculates the fewest number of operations needed to result in exactly n
    H characters in the file'''
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i


if __name__ == '__main__':
    from random import randint
    from time import time

    start_time = time()

    for i in range(10):
        n = randint(1, 100)
        print("{}: {}".format(n, minOperations(n)))

    print("--- {} seconds ---".format(time() - start_time))
