import random


class Contract:
    def __init__(self, job_list: list, prev_contract: object):
        """ Contract class
        Stores all information about a contract
        :param job_list: List of job numbers
        :param prev_contract: Previous contract in negotiation process
        """
        self.job_list = job_list
        self.__agent_accepted_list = []
        self.__agent_cost = []
        self.prev_contract = prev_contract

    def add_agent_decision(self, accepted: bool, cost: int):
        """ Save agent decision for current contract
        :param accepted: Has agent accepted this contract?
        :param cost: contract costs of agent
        """
        self.__agent_accepted_list.append(accepted)
        self.__agent_cost.append(cost)

    def get_agent_decisions(self) -> list:
        """ Get decisions of agents
        :return: list of all agent decisions
        """
        return self.__agent_accepted_list

    def get_agent_cost(self) -> list:
        """ Get costs for all agents
        :return: list of costs of every agent
        """
        return self.__agent_cost

    def get_diff_from_prev(self) -> list:
        """ Get the differences between the previous to current contract
        :return: list of all changed indices
        """
        diff = []
        for i in range(len(self.job_list)):
            if self.prev_contract.job_list[i] != self.job_list[i]:
                diff.append(i)

        return diff

    def refactor_new_contract(self, n_swaps) -> object:
        """ Swaps a desired amount of values in the list
        :param n_swaps: Number of swaps
        :return new_contract: Contract based on the previous agent decision
        """
        if False in self.__agent_accepted_list and self.prev_contract.prev_contract:
            new_contract = self.prev_contract.copy()
            diff = self.get_diff_from_prev()
        else:
            new_contract = self.copy()
            diff = []

        for i in range(n_swaps):
            pos_1 = random.randrange(0, len(self.job_list) - 1)
            pos_2 = random.randrange(0, len(self.job_list) - 1)

            # Executes if there more than two places that can be swapped
            if len(diff) < len(self.job_list) - 2:
                while pos_1 in diff:
                    pos_1 = random.randrange(0, len(self.job_list) - 1)
                while pos_2 in diff or pos_2 == pos_1:
                    pos_2 = random.randrange(0, len(self.job_list) - 1)

            new_contract.job_list[pos_2], new_contract.job_list[pos_1] \
                = new_contract.job_list[pos_1], new_contract.job_list[pos_2]

        return new_contract

    def copy(self) -> object:
        """ Copy current contract
        Create new contract having same job list and this contract as predecessor
        :return: new Contract
        """
        return Contract(self.job_list.copy(), self)

    def __len__(self) -> int:
        """ Get contract length
        :return: length of job list
        """
        return len(self.job_list)

    def __str__(self) -> str:
        """ Convert contract to string
        :return: returns job list as string
        """
        return str(self.job_list)
