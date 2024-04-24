#!/usr/bin/python3
'''operations to reach h num'''


def minOperations(n):
    '''minim'''
    if n <= 0:
        return 0
    ls = []

    def opr(n, ls):
        '''minim'''
        if n == 1:
            c = sum(ls)
            return c
        if n % 2 == 0:
            ls.append(2)
            return opr(n/2, ls)
        elif n % 3 == 0:
            ls.append(3)
            return opr(n/3, ls)
        elif n % 5 == 0:
            ls.append(5)
            return opr(n/5, ls)
        elif n % 7 == 0:
            ls.append(7)
            return opr(n/7, ls)
        else:
            ls.append(n)
            c = sum(ls)
            return c
    return opr(n, ls)
