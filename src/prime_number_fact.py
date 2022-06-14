import math


def sequentialFactorization(number):
    """Factorizacion secuencial de numeros primos"""
    primfac = []
    div = 2
    while div * div <= number:
        while (number % div) == 0:
            primfac.append(div)
            number //= div
        div += 1
    if number > 1:
        primfac.append(number)
    return primfac


def trialDivision(number):
    """Division por tentativa"""
    primfac = []
    while number % 2 == 0:
        primfac.append(2)
        number = number / 2
    i = 3
    max_factor = math.sqrt(number)
    while i <= max_factor:
        while number % i == 0:
            primfac.append(i)
            number = number / i
            max_factor = math.sqrt(number)
        i = i + 2
    if number > 1:
        primfac.append(number)
    return primfac
