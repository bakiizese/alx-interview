#!/usr/bin/python3
''' who wins in prime game '''


def isWinner(x, nums):
    ''' return winner '''
    meria = []
    ben = []
    for i in range(x):
        winner = Prime(1, nums[i])
        if winner == 0:
            ben.append(winner)
        else:
            meria.append(winner)
    if len(ben) > len(meria):
        return 'Ben'
    else:
        return 'Meria'


def Prime(start, end):
    ''' pick out the prime numbers '''
    nums = []
    prime = []
    count = 0

    for i in range(start, end + 1):
        nums.append(i)
    for i in nums:
        for j in nums:
            if i % j == 0:
                count += 1
        if count == 2:
            prime.append(i)
        count = 0
    if (len(prime) % 2 == 0):
        return 0
    else:
        return 1
