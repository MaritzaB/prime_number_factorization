import time
import random
import threading


def calculatePrimeFactors(n):
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


def main():
    print("Starting number crunching")
    t0 = time.time()

