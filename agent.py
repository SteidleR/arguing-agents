import math
import random
from contract import Contract


class Agent:
    def __init__(self, agent_name: str, file_name_costs: str):
        """ Agent class
        Argues about contracts all day
        :param agent_name: Identifying string
        :param file_name_costs: Nome of the file including a cost matrix
        """
        self.name = agent_name
        self.cost_matrix = Agent.read_cost_matrix(file_name_costs)
        self.n = len(self.cost_matrix)
        self.temperature = 1

    def calc_temp(self, required_accept_rate: float, n_trial: int = 100):
        """ Calculate the temperature according to the new minimal acceptance rate
        :param required_accept_rate: Percentage for how many contracts need to be accepted
        :param n_trial: Number of loops for the contract delta
        """
        delta_cost = 0

        last_job_list = random.sample(list(range(0, self.n)), self.n)
        for i in range(0, n_trial):
            job_list = random.sample(list(range(0, self.n)), self.n)

            costs_last = self._evaluate_cost(last_job_list)
            costs = self._evaluate_cost(job_list)

            delta_cost += abs(costs - costs_last)

            last_job_list = job_list

        temp = (delta_cost/n_trial) / math.log(required_accept_rate)
        self.temperature = temp

    def accept_contract_fink(self, contract: Contract) -> (bool, int):
        """ Decide whether to accept a contract or not based on Andreas Fink's work
        :param contract: List of unique integer values representing jobs ranging from 0 to n
        :returns
            accept: Was the contract accepted?
            cost: Cost of the new contract
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

    def _evaluate_cost(self, job_list: list) -> int:
        """ Calculates the costs for a contract
        :param job_list: List of unique integer values representing jobs ranging from 0 to n
        :return costs: Absolute value for the costs
        """
        costs = 0
        for i in range(len(job_list)-1):
            costs += self.cost_matrix[job_list[i]][job_list[i+1]]
        return costs

    @staticmethod
    def read_cost_matrix(file_name_costs: str) -> list:
        """ Read cost matrix from text file
        :param file_name_costs: file name/path to cost matrix
        :return matrix: 2d cost matrix
        """
        matrix = []
        with open(file_name_costs, "r") as f:
            for line in f.readlines()[1:]:
                matrix.append([int(i) for i in line.replace(" \n", "").split(" ")])
        return matrix
