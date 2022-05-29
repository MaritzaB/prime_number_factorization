from prime_number_fact import calculatePrimeFactors
from N17_euclidex1 import euclidex1, euclidex
import time
from random import getrandbits, seed
import matplotlib.pyplot as plt
import numpy as np
import math


def listOfRandbits():
    seed(68)
    randbits_list = []
    for i in range(1,60):
        randbits_list.append(getrandbits(i))
    return randbits_list


def timer(function, number):
    init_time = time.time()
    function(number)
    final_time = time.time()
    total_time = final_time - init_time
    return total_time


rand_num_list = listOfRandbits()
timer_list = []

for i in range(len(rand_num_list)):
    print(f"Número aleatorio: ", rand_num_list[i], "Bits: ", math.floor(math.log(rand_num_list[i])))
    timer_list.append(timer(calculatePrimeFactors, rand_num_list[i]))
    print(f"Tiempo de cálculo: ", timer(calculatePrimeFactors, rand_num_list[i]))


# Plot practical complexity
plt.xlabel('Bits')
plt.ylabel('Tiempo (segundos)')
plt.title('Complejidad práctica')
bits = [x for x in range(1,60)]

plt.plot(bits,timer_list)
plt.savefig("practical_complexity.png")

# Clear the figure
plt.clf()
