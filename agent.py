

class Agent:
    def __init__(self, file_name_costs):
        self.cost_matrix = Agent.read_cost_matrix(file_name_costs)

    def evaluate_cost(self, contract):
        pass

    @staticmethod
    def read_cost_matrix(file_name_costs):
        matrix = []
        first_line = True
        with open(file_name_costs, "r") as f:
            for line in f.readlines():
                if not first_line:
                    matrix.append([int(i) for i in line.replace(" \n", "").split(" ")])
                else:
                    first_line = False
        return matrix
