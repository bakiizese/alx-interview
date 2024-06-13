#!/usr/bin/python3
''' count coins '''


def makeChange(coins, total):
    ''' make change '''
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    cg = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            cg += 1
        if (total == 0):
            return cg
    return -1
