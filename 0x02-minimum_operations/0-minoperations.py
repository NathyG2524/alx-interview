#!/usr/bin/python3
"""
find the minimun operation
"""


def isprime(n):
    """ check id n is prime"""
    if (n < 2):
        return False
    elif (n == 2):
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def minOperations(n):
    """minimum operations"""
    listFac = []
    if n == 1:
        return 1
    for i in range(2, int(n)+1):
        while (n % i == 0):
            if (isprime(i)):
                listFac.append(i)
            n = n / i

    lisum = 0
    for i in listFac:
        lisum = lisum + i

    return lisum
