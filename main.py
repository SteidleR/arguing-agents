import logging
logging.basicConfig(level=logging.DEBUG)

from agent import Agent
from mediator import Mediator


A = Agent("data/daten2A.txt")
B = Agent("data/daten2B.txt")

mediator = Mediator(10)

try:
    last_contract = mediator.generate_new_contract()
    while True:
        contract = mediator.generate_new_contract()
        accept_a = A.accept_contract_fink(contract, last_contract)
        accept_b = B.accept_contract_fink(contract, last_contract)

        last_contract = contract

        if accept_a and accept_b:
            break

    print("Accepted contract: ", contract)

except KeyboardInterrupt:
    print("Cancelled...")
