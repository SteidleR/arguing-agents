import seaborn as sns
import matplotlib.pyplot as plt


from agent import Agent
from mediator import Mediator


MAX_CONTRACTS = 2000

STEP_DOWN = 100

JOB_SWAPS = 5

A = Agent("🅰️", "data/daten3A.txt")
B = Agent("🅱️", "data/daten3B.txt")

mediator = Mediator([A, B], MAX_CONTRACTS, STEP_DOWN, JOB_SWAPS)
mediator.run_negotiation_process()

for line in range(len(mediator.costs_per_round)):
    sns.lineplot(x=list(range(len(mediator.costs_per_round[0]))), y=mediator.costs_per_round[line])
plt.show()
