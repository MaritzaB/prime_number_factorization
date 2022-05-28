import math


def euclidex1(a, b):
    # Calcula en forma iterativa
    Q = a // b
    A = 0
    B = 1
    C = 1
    D = -Q
    while a % b != 0:
        bx = b
        b = a % b
        a = bx
        Q = a // b
        Ax = C
        Bx = D
        C = A - Q * C
        D = B - Q * D
        A = Ax
        B = Bx
    return A, B, b


# print("El máximo común divisor entre 18 y 12",euclidex1(18,12))


def euclidex(a, b):
    # Calcula de forma recursiva
    if a % b == 0:
        return 0, 1, b
    else:
        A, B, r = euclidex(b, a % b)
        return B, A - (a // b) * B, r


# print("El máximo común divisor entre 18 y 12",euclidex(18,12))


def euclides(a, b):
    if a % b == 0:
        return b
    else:
        return euclides(b, a % b)


# Def phi de euler


def phi(n):
    m = 0
    for k in range(1, n):
        if euclides(n, k) == 1:
            m = m + 1
    return m


# print(phi(18))


def chino(m, r):
    M = 1
    Mi = []
    Yi = []
    k = len(m)
    for i in range(k):
        M = M * m[i]
    for i in range(k):
        Mi = Mi + [M / m[i]]
    for i in range(k):
        A, B, C = euclidex(Mi[i], m[i])
        Yi = Yi + [A]
    X = 0
    for i in range(k):
        X = X + Yi[i] * Mi[i] * r[i]
    return X % M


def facp(n):  # Encontrar coordenadas primas
    e = []
    if n == 1:
        return [0]
    i = 0
    while n != 1:
        k = 0
        while n % p[i] == 0:
            k = k + 1
            n = n // p[i]
        e = e + [k]
        i = i + 1
    return e


# 19 de mayo. Teorema de Euler.
# Medir la complejidad práctica y compararla con n**2 (debe de ser menor)


def criba(n):
    a = [x for x in range(n)]
    ap = []
    i = 2
    imax = math.sqrt(n)
    while i < imax:
        k = 2
        while k * a[i] < n:
            a[k * a[i]] = 0
            k = k + 1
        i = i + 1
        while a[i] == 0:
            i = i + 1
    for j in range(2, n):
        if a[j] != 0:
            ap = ap + [a[j]]
    return ap  # Lista de números primos menores que n


def number(e):
    n = len(e)
    m = 1
    for i in range(n):
        m = m * (p[i] ** e[i])
    return m


n = 100
p = criba(n)  # p lo usa facp
# print("Criba de {n} \n", criba(n),"\n")

# print("Encontrar coordenadas primas", facp(n),"\n")

# print(number(criba(n)),"\n")
