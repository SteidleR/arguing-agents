from agent import Agent
from mediator import Mediator


MAX_CONTRACTS = 2000

START_PROB = 0.8
END_PROB = 0.1
PROB_STEP_DOWN = 0.1

A = Agent("🅰️", "data/daten3A.txt")
B = Agent("🅱️", "data/daten3B.txt")

mediator = Mediator([A, B], MAX_CONTRACTS, START_PROB, END_PROB, PROB_STEP_DOWN)
mediator.run_negotiation_process()
