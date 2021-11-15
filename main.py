import logging
logging.basicConfig(level=logging.DEBUG)

from agent import Agent


A = Agent("data/daten2A.txt")
B = Agent("data/daten2B.txt")

print(A.cost_matrix)
print(B.cost_matrix)

contract_last = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
contract = [0, 1, 2, 4, 7, 6, 3, 9, 5, 8]

print(A.accept_contract_fink(contract, contract_last))
print(B.accept_contract_fink(contract, contract_last))
