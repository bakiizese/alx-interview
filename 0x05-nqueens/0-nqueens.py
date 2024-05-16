#!/usr/bin/python3
''' nquuens '''
import sys
result = []


def nqueen(n, row, diags, anti_diags, cols, checked):
    ''' return possible sol '''
    if row == n:
        result.append(checked.copy())
        return checked
    for col in range(n):
        diag = row - col
        anti_diag = row + col
        if col in cols or diag in diags or anti_diag in anti_diags:
            continue

        checked.append([row, col])
        diags.append(diag)
        anti_diags.append(anti_diag)
        cols.append(col)

        nqueen(n, row + 1, diags, anti_diags, cols, checked)

        checked.pop()
        diags.remove(diag)
        anti_diags.remove(anti_diag)
        cols.remove(col)
    return None


def nqueens():
    ''' nqueens '''
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print(f'Usage: nqueens N')
        return 1
    n = sys.argv[1]
    try:
        n = int(n)
    except Exception:
        print(f'N must be a number')
        return 1
    if n < 4:
        print(f'N must be at least 4')
        return 1
    nqueen(n, row=0, diags=[], anti_diags=[], cols=[], checked=[])
    for i in result:
        print(i)


if __name__ == '__main__':
    nqueens()
