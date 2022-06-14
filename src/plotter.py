import matplotlib.pyplot as plt
import numpy as np
from analizer import timeScorer
from prime_number_fact import sequentialFactorization as sf, trialDivision as td


def complexityPlotter(max_bits, comparative_table, filepath):
    """Grafica complejidad practica"""
    plt.xlabel("Tamano de n (bits)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Complejidad practica")
    plt.xscale("log")
    plt.yscale("log")
    bits = list(range(1, max_bits))
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
    bits = list(range(1, max_bits))
    ratio = np.array(comparative_table[0] / comparative_table[1])
    plt.plot(bits, ratio)
    plt.axhline(y=1, color="r", linestyle="--")
    plt.legend()
    plt.savefig(filepath)
    plt.clf()


def pickWinner(seq_fact_list, trial_div_list):
    winner_table = []
    for i in range(1, len(seq_fact_list)):
        if seq_fact_list[i] < trial_div_list[i]:
            winner_table.append("Factorizacion secuencial")
        else:
            winner_table.append("Division tentativa")
    winner_table = np.array(winner_table)
    return winner_table


sequential_fact_list = np.array(timeScorer(sf))
trial_division_list = np.array(timeScorer(td))

# Pick winner
winner = np.array(pickWinner(sequential_fact_list, trial_division_list))

# Fill table
time_score_table = []
time_score_table.append(sequential_fact_list)
time_score_table.append(trial_division_list)
time_score_table = np.array(time_score_table)

COMPLEXITY_FIG_PATH = "reports/figures/practical_complexity.png"
RATIO_FIG_PATH = "reports/figures/ratio.png"
MAX_BITS = 50

# Plot complexity
complexityPlotter(MAX_BITS, time_score_table, COMPLEXITY_FIG_PATH)

# Plot ratio
ratioPlotter(MAX_BITS, time_score_table, RATIO_FIG_PATH)
