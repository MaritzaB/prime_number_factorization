from prime_number_fact import sequentialFactorization, trialDivision
from random import getrandbits, seed
import math
import numpy as np
import pandas as pd
import time

max_bits = 50


def randBits(max_bits):
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
    rand_num_list = randBits(max_bits)
    time_score = []
    for i in range(len(rand_num_list)):
        time_score.append(timer(factFunction, rand_num_list[i]))
    return time_score
