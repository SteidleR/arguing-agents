import seaborn as sns
import matplotlib.pyplot as plt


from agent import Agent
from mediator import Mediator


MAX_CONTRACTS = 2000

START_PROB = 1.001
END_PROB = 0.01
PROB_STEP_DOWN = 0.25

JOB_SWAPS = 5

A = Agent("🅰️", "data/daten3A.txt")
B = Agent("🅱️", "data/daten3B.txt")

mediator = Mediator([A, B], MAX_CONTRACTS, START_PROB, END_PROB, PROB_STEP_DOWN, JOB_SWAPS)
mediator.run_negotiation_process()

for line in range(len(mediator.costs_per_round)):
    sns.lineplot(x=list(range(len(mediator.costs_per_round[0]))), y=mediator.costs_per_round[line])
plt.show()
