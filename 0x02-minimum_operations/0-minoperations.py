#!/usr/bin/python3
'''operations to reach h num'''


def minOperations(n):
    '''minim'''
    if n < 2:
        return 0
    ls = 2
    op = 0
    while n >= ls:
        if n % ls == 0:
            n /= ls
            op += ls
            ls -= 1
        ls += 1
    return op
