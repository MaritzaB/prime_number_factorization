from analizer import timeScorer, max_bits
from pathlib import Path
from prime_number_fact import sequentialFactorization, trialDivision
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

max_bits = 50
# filepath = Path("reports/table/out.csv")


seq_fact_list = np.array(timeScorer(sequentialFactorization))
trial_div_list = np.array(timeScorer(trialDivision))

time_score_table = [seq_fact_list, trial_div_list]


def plotter(max_bits):
    """Grafica complejidad practica"""
    plt.xlabel("Tamaño de n (bits)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Complejidad práctica")
    bits = [x for x in range(1, max_bits + 1)]
    for nlist in time_score_table:
        plt.plot(bits, nlist)
        plt.savefig("practical_complexity.png")


plotter(max_bits)


# def ratio(seq_fact_list, trial_div_list):
#    for i in range(len(seq_fact_list)):
#        if seq_fact_list[i] < trial_div_list[i]:
#            print("gana lista1")
#        else:
#            print("gana lista2")


# ratio = ratio(seq_fact_list, trial_div_list)

# time_score_table.append(ratio)

# lambdas_table = pd.DataFrame(time_score_table)  # .pivot(columns='Date', values='Value')

# lambdas_table.columns = ["Islet", "Growth_rate", "p_value", "p_value_menor"]

# lambdas_table.to_csv(filepath, index=False)
