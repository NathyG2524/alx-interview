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


def isfdivisible_by2(n):
    """check for fully divisible by 2"""
    if n == 2:
        return True
    if n % 2 == 0:
        return isfdivisible_by2(n / 2)
    else:
        return False


def isdivisible_by2(n):
    """check divisible by 2"""
    if n < 2:
        return False
    if n % 2 == 0:
        return True
    else:
        return False


def isdivisible_by3(n):
    """check divisible by 3"""
    if n < 3:
        return False
    if n % 3 == 0:
        return True
    else:
        return False


def count_no_iteration(n, d):
    """check for iteration"""
    count = 0
    i = n
    while(i % d == 0):

        count = count + 1
        i = i / d

        if isprime(int(i)):
            count = (2 * count) + int(i)
            break

    return count


def minOperations(n):
    """count minmum operation"""
    if n < 1:
        return 0
    if n == 1:
        return 1
    if (isprime(n)):
        return n
    if (isfdivisible_by2(n)):
        count = count_no_iteration(n, 2)
        return count * 2

    if isdivisible_by3(n) and isdivisible_by2(n):
        count = count_no_iteration(n, 2)
        return (count * 2 + 3)

    if isdivisible_by3(n) and not isdivisible_by2(n):
        return int(n / 3 + 3)

    if (n % 2 == 0):
        return count_no_iteration(n, 2)


print(minOperations(9))
