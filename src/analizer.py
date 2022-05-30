from prime_number_fact import calculatePrimeFactors, wheelFact, main
import time
from random import getrandbits, seed
import matplotlib.pyplot as plt
import numpy as np
import math

max_bits = 50


def listOfRandbits(max_bits):
    seed(68)
    randbits_list = []
    for i in range(1, max_bits):
        randbits_list.append(getrandbits(i))
    return randbits_list


def timer(function, number):
    init_time = time.time()
    function(number)
    final_time = time.time()
    total_time = final_time - init_time
    return total_time


def timeScorer(factFunction):
    rand_num_list = listOfRandbits()
    timer_list_Prime_Factors = []
    for i in range(len(rand_num_list)):
        timer_list_Prime_Factors.append(timer(factFunction, rand_num_list[i]))
    return timer_list_Prime_Factors




### Plot practical complexity
# plt.xlabel('Bits')
# plt.ylabel('Tiempo (segundos)')
# plt.title('Complejidad práctica')
# bits = [x for x in range(1,max_bits)]
#
# plt.plot(bits,timer_list_Prime_Factors)
# plt.plot(bits,timer_list_Prime_wheelFact)
# plt.savefig("practical_complexity.png")
#
### Clear the figure
##plt.clf()
