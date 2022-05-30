from analizer import timeScorer
from pathlib import Path
from prime_number_fact import sequentialFactorization, trialDivision
import numpy as np
import pandas as pd

filepath = Path("reports/table/out.csv")


list1 = np.array(timeScorer(sequentialFactorization))
list2 = np.array(timeScorer(trialDivision))

time_score_table = [list1, list2]


def ratio(list1, list2):
    for i in range(len(list1)):
        if list1[i] < list2[i]:
            print("gana lista1")
        else:
            print("gana lista2")


ratio = ratio(list1, list2)

# time_score_table.append(ratio)

lambdas_table = pd.DataFrame(time_score_table)  # .pivot(columns='Date', values='Value')

# lambdas_table.columns = ["Islet", "Growth_rate", "p_value", "p_value_menor"]

lambdas_table.to_csv(filepath, index=False)

# Plot practical complexity
# plt.xlabel('Bits')
# plt.ylabel('Tiempo (segundos)')
# plt.title('Complejidad práctica')
# bits = [x for x in range(1,max_bits)]
#
# plt.plot(bits,timer_list_Prime_Factors)
# plt.plot(bits,timer_list_Prime_trialDivision)
# plt.savefig("practical_complexity.png")
#
# Clear the figure
