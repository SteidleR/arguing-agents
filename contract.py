import random


class Contract:
    def __init__(self, job_list, prev_contract):
        self.job_list = job_list
        self.__agent_accepted_list = []
        self.__agent_cost = []  # todo not access! delete in the end 🚨
        self.prev_contract = prev_contract

    def add_agent_decision(self, accepted, cost):
        self.__agent_accepted_list.append(accepted)
        self.__agent_cost.append(cost)

    def get_diff_from_prev(self) -> list:
        """ Get the differences between the previous to current contract
        :return: list of all changed indices
        """
        diff = []
        for i in range(len(self.job_list)):
            if self.prev_contract.job_list[i] != self.job_list[i]:
                diff.append(i)

        return diff

    def refactor_new_contract(self, n_swaps):
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

    def copy(self):
        return Contract(self.job_list.copy(), self)

    def __len__(self):
        return len(self.job_list)

    def __str__(self):
        return str(self.job_list)
