#!/usr/bin/python3
'''island'''
from collections import Counter
rows = []
cols = []


def island_perimeter(grid):
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                rows.append(i)
                cols.append(j)
    freqc = Counter(cols)
    most_fc = freqc.most_common(1)
    freqr = Counter(rows)
    most_fr = freqr.most_common(1)
    n = most_fc[0][1]
    m = most_fr[0][1]
    return n * m + n
