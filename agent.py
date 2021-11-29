import math
import random
from contract import Contract


class Agent:
    def __init__(self, agent_name, file_name_costs):
        self.name = agent_name
        self.cost_matrix = Agent.read_cost_matrix(file_name_costs)
        self.n = len(self.cost_matrix)
        self.temperature = 1

    def calc_temp(self, required_accept_rate, n_trial=1000):
        """ Calculate the temperature according to the new minimal acceptance rate
        :param required_accept_rate: Percentage for how many contracts need to be accepted
        :param n_trial: Number of loops for the contract delta
        """
        delta_cost = 0

        last_contract = random.sample(list(range(0, self.n)), self.n)
        for i in range(0, n_trial):
            contract = random.sample(list(range(0, self.n)), self.n)

            costs_last = self._evaluate_cost(last_contract)
            costs = self._evaluate_cost(contract)

            delta_cost += abs(costs - costs_last)

            last_contract = contract

        temp = (delta_cost/n_trial) / math.log(required_accept_rate)
        self.temperature = temp

    def accept_contract_fink(self, contract: Contract) -> (bool, int):
        """ Decide whether to accept a contract or not based on Andreas Fink's work
        :param contract: List of unique integer values representing jobs ranging from 0 to n
        :return
            bool: Was the contract accepted?
            int: Cost of the new contract
        """
        cost = self._evaluate_cost(contract.job_list)
        prev_cost = self._evaluate_cost(contract.prev_contract.job_list)

        if prev_cost >= cost:
            # print(f"{self.name} {prev_cost} -> {cost} ACCEPT BY DEFAULT")
            return True, cost
        else:
            prob = math.e ** ((cost - prev_cost) / self.temperature)
            random_decision = random.random()
            accept = random_decision < prob
            # print(f"{self.name} {prev_cost} -> {cost} {'ACCEPT' if accept else 'DECLINE'} WITH PROB {1-prob}")
            return accept, cost

    def _evaluate_cost(self, contract):
        """ Calculates the costs for a contract
        :param contract: List of unique integer values representing jobs ranging from 0 to n
        :return: costs: Absolute value for the costs
        """
        costs = 0
        for i in range(len(contract)-1):
            costs += self.cost_matrix[contract[i]][contract[i+1]]
        return costs

    @staticmethod
    def read_cost_matrix(file_name_costs):
        """ Read cost matrix from text file
        :param file_name_costs: file name/ path to cost matrix
        :return: 2d cost matrix
        """
        matrix = []
        with open(file_name_costs, "r") as f:
            for line in f.readlines()[1:]:
                matrix.append([int(i) for i in line.replace(" \n", "").split(" ")])
        return matrix
