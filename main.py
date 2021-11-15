from agent import Agent


A = Agent("data/daten2A.txt")
B = Agent("data/daten2B.txt")

print(A.cost_matrix)
print(B.cost_matrix)

contract = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(A.evaluate_cost(contract))
print(B.evaluate_cost(contract))
