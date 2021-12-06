import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import time

from agent import Agent
from mediator import Mediator

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––– Defining negotiation conditions ––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

MAX_CONTRACTS = 30000
TEMPERATURE_INTERVAL = 500
JOB_SWAPS = 1

A = Agent("🅰️", "data/daten3A.txt")
B = Agent("🅱️", "data/daten3B.txt")

mediator = Mediator([A, B], MAX_CONTRACTS, TEMPERATURE_INTERVAL, JOB_SWAPS)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––– Negotiation process ––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

t1 = time.time()
mediator.run_negotiation_process()
print("Dauer:", time.time() - t1)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ––––––––––––––––– Plotting results –––––––––––––––––––––––––––––––––
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

matplotlib.rcParams["figure.dpi"] = 500

for line in range(len(mediator.costs_per_round)):
    sns.lineplot(x=list(range(len(mediator.costs_per_round[0]))), y=mediator.costs_per_round[line], linewidth=.1)
plt.grid()
plt.show()
