import random
from contract import Contract


class Mediator:
    def __init__(self, agent_list: list, max_contracts: int = 1000, temp_interval: int = 10, job_swaps: int = 1):
        """ Mediator class
        Runs the negotiation process and handles contracts
        :param agent_list: List of all contributing agents
        :param max_contracts: Max number of negotiation rounds
        :param temp_interval: Interval of rounds after which temperature changes
        :param job_swaps: Number of jobs that will be swapped in a contract
        """
        self.agent_list = agent_list

        self.base_contract = random.sample(list(range(agent_list[0].n)), agent_list[0].n)
        self.contracts = [Contract(self.base_contract, None)]
        self.contracts[-1].add_agent_decision(True, 0)
        self.contracts.append(Contract(self.base_contract, self.contracts[-1]))
        self.contracts[-1].add_agent_decision(True, 0)
        self.max_contracts = max_contracts

        self.step_down = temp_interval
        self.job_swaps = job_swaps

        self.current_prob = 1.0

        self.rounds = []
        self.costs_per_round = [[] for _ in range(len(agent_list)+1)]

    def run_negotiation_process(self):
        """ Executes a full negotiation with multiple rounds
        """
        for n in range(0, self.max_contracts):
            try:
                self._round_of_negotiation(n)
            except Exception as e:
                print(e)
                break

        print("\n🎉 🥳 🎊 Final accepted contract 🪅 🍻 🍾")

        last_contract = self.contracts[-1]
        if False in last_contract.get_agent_decisions():
            best_contract = last_contract.prev_contract
        else:
            best_contract = last_contract

        print("📃", best_contract.job_list)

        cost = best_contract.get_agent_cost()
        for i, agent in enumerate(self.agent_list):
            print(agent.name + ": " + str(cost[i]))
        print("Sum of costs: " + str(sum(cost)))

    def _round_of_negotiation(self, round_n: int):
        """ Single round of negotiation process
        :param round_n: current round number
        """
        if round_n % self.step_down == 0:
            self._adjust_temperature()
            print(f"\n⚜️ ⚜️ ⚜️ Round: {round_n} ⚜️ ⚜️ ⚜️")

        print(f"\n⚜️ ⚜️ ⚜️ Round: {round_n} ⚜️ ⚜️ ⚜️")
        contract = self.contracts[-1].refactor_new_contract(self.job_swaps)
        print("📃", contract)

        for i, agent in enumerate(self.agent_list):
            acc, cost = agent.accept_contract_fink(contract)
            contract.add_agent_decision(acc, cost)
            self.costs_per_round[i].append(cost)
        self.costs_per_round[-1].append(sum(contract.get_agent_cost()))

        self.contracts.append(contract)

    def _adjust_temperature(self):
        """ Adjust temperature for all agents
        """
        if self.current_prob < 1.0e-90:
            return
        self.current_prob /= 2
        print(f"\n🥵 Temperatures are cooling for probability {self.current_prob} 🥶")
        for agent in self.agent_list:
            agent.calc_temp(self.current_prob)
