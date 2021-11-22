import random


class Mediator:
    def __init__(self, n_contracts: int):
        self.base_contract = list(range(n_contracts))
        self.contracts = []

    def generate_new_contract(self):
        while True:
            contract = random.sample(self.base_contract, len(self.base_contract))
            if contract not in self.contracts:
                return contract
