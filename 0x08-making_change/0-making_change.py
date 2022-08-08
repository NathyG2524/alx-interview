#!/usr/bin/python3

"""
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
"""
def makeChange(coins, total):
    """return: fewest number of coins needed to meet total"""
    sort = sorted(coins)
    rever = sort[::-1]
    ans = 0
    for i in rever:
        if total > i:
            result = int(total / i)
            total = total % i
            ans = ans + result
    if total == 0:
        return(ans)
    else:
        return(-1)
