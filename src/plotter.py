from analizer import timeScorer, max_bits
from pathlib import Path
from prime_number_fact import sequentialFactorization, trialDivision
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

max_bits = 50


def complexityPlotter(max_bits, comparative_table, filepath):
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
    plt.savefig(filepath)
    plt.clf()


def ratioPlotter(max_bits, comparative_table, filepath):
    """Grafica la razon deproporcion en que un
    algoritmo es mas rapido que otro"""
    plt.xlabel("Tamano de n (bits)")
    plt.ylabel("Razon")
    plt.title("Razon de proporcion")
    plt.xscale("log")
    bits = [x for x in range(1, max_bits + 1)]
    ratio = np.array(comparative_table[0] / comparative_table[1])
    plt.plot(bits, ratio)
    plt.axhline(y=1, color="r", linestyle="--")
    plt.legend()
    plt.savefig(filepath)
    plt.clf()


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

# Pick winner
winner = np.array(pickWinner(seq_fact_list, trial_div_list))

# Fill table
time_score_table = []
time_score_table.append(seq_fact_list)
time_score_table.append(trial_div_list)
time_score_table = np.array(time_score_table)

complexity_fig_path = "reports/figures/practical_complexity.png"
ratio_fig_path = "reports/figures/ratio.png"

# Plot complexity
complexityPlotter(max_bits, time_score_table, complexity_fig_path)

# Plot ratio
ratioPlotter(max_bits, time_score_table, ratio_fig_path)
