import time
import math


def sequentialPrimeFactorization(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac


def trialDivision(n):
    primfac = []
    while n % 2 == 0:
        primfac.append(2)
        n = n / 2
    i = 3
    max_factor = math.sqrt(n)
    while i <= max_factor:
        while n % i == 0:
            primfac.append(i)
            n = n / i
            max_factor = math.sqrt(n)
        i = i + 2
    if n > 1:
        primfac.append(n)
    return primfac
