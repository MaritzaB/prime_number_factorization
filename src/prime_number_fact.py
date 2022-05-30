import time
import random
import threading
import math


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


def executeProcess():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculatePrimeFactors(rand))


def main():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=executeProcess)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def wheelFact(n):
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
