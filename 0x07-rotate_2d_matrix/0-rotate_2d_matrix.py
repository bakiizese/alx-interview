#!/usr/bin/python3
''' rotate 2d matrix clock-wise '''


def rotate_2d_matrix(matrix):
    ''' rotate 2d matrix in 90 degrees '''
    n = len(matrix)
    ls_all = []
    ls = []
    for i in range(n):
        for j in range(n):
            ls.append([j, i])
        ls_all.append(ls.copy())
        ls = []
    ks = []
    ls = []
    for i in ls_all:
        for j in i:
            a = j[0]
            b = j[1]
            ls.append(matrix[a][b])
        ls.reverse()
        ks.append(ls.copy())
        ls = []
    for i in range(n):
        matrix[i] = ks[i]
