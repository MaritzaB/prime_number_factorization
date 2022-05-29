from prime_number_fact import criba, number, euclides, euclidex, euclidex1, phi
import time
from random import getrandbits
import numpy as np

# Generar lista de números aleatorios basados en bits
lista = []
for i in [2,5,10,15,20,25,30,35,40]:
    lista.append(getrandbits(i))

print(lista)

first_number = 15
second_number = 27
numbers = (first_number, second_number)
n=48
#print(f'phi de {n} es ',phi(n))
#print(f'Criba de {n} es', criba(n))
#
print(euclidex(first_number, second_number))
print(euclidex1(first_number, second_number))
#print(euclides(first_number, second_number))

def timer(function, numbers):
    init_time = time.time_ns()
    function(numbers[0], numbers[1])
    final_time = time.time_ns()
    total_time = final_time - init_time
    return total_time


run_times = 15
time_euclidex = []
time_euclidex1 = []
time_euclides = []

for r in range(run_times):
    time_euclidex.append(timer(euclidex, numbers))
    time_euclidex1.append(timer(euclidex1, numbers))
    time_euclides.append(timer(euclides, numbers))
    # print(f"Run number {r} for {euclidex.__name__}",timer(euclidex, numbers))
    # print(f"Run number {r} for {euclidex1.__name__}",timer(euclidex1, numbers))
    # print(f"Run number {r} for {euclides.__name__}",timer(euclides, numbers))
    # print("-----\n")

#print(time_euclidex, "\n", time_euclidex1, "\n", time_euclides)
