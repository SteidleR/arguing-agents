

class Agent:
    def __init__(self, file_name_costs):
        self.cost_matrix = Agent.read_cost_matrix(file_name_costs)

    def evaluate_cost(self, contract):
        """
        Calculates the costs for a series of jobs.
        :param contract:
        :return: costs as
        """
        costs = 0
        for i in range(len(contract)-1):
            costs += self.cost_matrix[i][i+1]
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
