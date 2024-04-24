#!/usr/bin/python3
'''operations to reach h num'''


def minOperations(n):
    '''minim'''
    if n <= 0:
        return 0
    ls = 0

    def opr(n, ls):
        '''minim'''
        if n == 1:
            return int(ls)
        if n % 2 == 0:
            ls += 2
            return opr(n/2, ls)
        elif n % 3 == 0:
            ls += 3
            return opr(n/3, ls)
        elif n % 5 == 0:
            ls += 5
            return opr(n/5, ls)
        elif n % 7 == 0:
            ls += 7
            return opr(n/7, ls)
        else:
            ls += n
            return int(ls)
    return opr(n, ls)
