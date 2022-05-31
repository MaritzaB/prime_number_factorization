from analizer import timeScorer, max_bits
from pathlib import Path
from prime_number_fact import sequentialFactorization, trialDivision
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

max_bits = 50


def plotter(max_bits, comparative_table):
    """Grafica complejidad practica"""
    plt.xlabel("Tamano de n (bits)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Complejidad practica")
    plt.xscale("log")
    plt.yscale("log")
    bits = [x for x in range(1, max_bits + 1)]
    plt.plot(bits, comparative_table[0], label="Factorizacion secuencial")
    plt.plot(bits, comparative_table[1], label="Division tentativa")
    plt.legend()
    plt.savefig("reports/figures/practical_complexity.png")


def pickWinner(seq_fact_list, trial_div_list):
    winner_table = []
    for i in range(len(seq_fact_list)):
        if seq_fact_list[i] < trial_div_list[i]:
            winner_table.append("Factorizacion secuencial")
        else:
            winner_table.append("Division tentativa")
    winner_table = np.array(winner_table)
    return winner_table


seq_fact_list = np.array(timeScorer(sequentialFactorization))
trial_div_list = np.array(timeScorer(trialDivision))

# Calculate ratio between algorithms
ratio = np.array(trial_div_list / seq_fact_list)

# Pick winner
winner = np.array(pickWinner(seq_fact_list, trial_div_list))

# Fill table
time_score_table = []
# time_score_table.append(ratio)
time_score_table.append(seq_fact_list)
time_score_table.append(trial_div_list)
# time_score_table.append(winner)

time_score_table = np.array(time_score_table)

# pd.DataFrame(time_score_table).to_csv("file.csv", index=False)

# time_score_table = pd.DataFrame(time_score_table)


# Plot complexity
plotter(max_bits, time_score_table)

# time_score_table.to_csv(filepath, index=False)
