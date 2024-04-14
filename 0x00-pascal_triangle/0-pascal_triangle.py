#!/usr/bin/python3
'''pascal's triang;e'''


def pascal_triangle(n):
    '''returns list'''
    if n <= 0:
        return []

    ls = []
    ls1 = [0, 1, 0]
    t = 0

    for count in range(n):
        ls.append(ls1)
        ls2 = []
        b = 0

        for b in range(len(ls1) - 1):
            c = ls1[b] + ls1[b + 1]
            ls2.append(c)
        ls2.append(t)
        ls2.insert(0, t)
        ls1 = ls2

    rmls = [[x for x in sublist if x != 0] for sublist in ls]
    return rmls

