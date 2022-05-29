from prime_number_fact import calculatePrimeFactors
from N17_euclidex1 import euclidex1, euclidex
import time
from random import getrandbits, seed
import numpy as np
import math


def listOfRandbits():
    seed(68)
    randbits_list = []
    for i in [3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 63]:
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
    timer_list.append(timer(calculatePrimeFactors,rand_num_list[i]))
    print(f"Tiempo de cálculo: ", timer(calculatePrimeFactors, rand_num_list[i]))


run_times = 15
time_1st_algorithm = []


# for r in range(run_times):
#    time_1st_algorithm.append(timer(euclidex, numbers))

# print(f"Run number {r} for {euclidex.__name__}",timer(euclidex, numbers))
# print(f"Run number {r} for {euclidex1.__name__}",timer(euclidex1, numbers))
# print(f"Run number {r} for {euclides.__name__}",timer(euclides, numbers))
# print("-----\n")

# print(time_euclidex, "\n", time_euclidex1, "\n", time_euclides)
