from random import getrandbits, seed
import time


def randBits(max_bits):
    """Genera una lista de numeros enteros aleatorios
    cuyos elementos aumentan en el tamano de las cifras"""
    seed(68)
    randbits_list = []
    for i in range(1, max_bits + 1):
        randbits_list.append(getrandbits(i))
    return randbits_list


def timer(function, number):
    """Toma el tiempo de ejecucion de un
    algoritmo para un numero dado"""
    init_time = time.time()
    function(number)
    final_time = time.time()
    total_time = final_time - init_time
    return total_time


MAX_BITS = 50


def timeScorer(factorization_function):
    """Toma el tiempo de ejecucion de un
    algoritmo para una lista de numeros dados"""
    rand_num_list = randBits(MAX_BITS)
    time_score = []
    for i in range(len(rand_num_list)):
        time_score.append(timer(factorization_function, rand_num_list[i]))
    return time_score
