import random
from contract import Contract


class Mediator:
    def __init__(self,
                 agent_list: list,
                 max_contracts: int = 1000,
                 start_prob: float = 0.9,
                 end_prob: float = 0.1,
                 prob_step: float = 0.1,
                 job_swaps: int = 1):
        """
        :param agent_list: list of agents
        :param n_jobs: number of jobs
        :param max_contracts: max number of negotiation rounds
        :param start_prob: starting probability
        :param end_prob: final probability
        :param prob_step: probability step down
        """
        self.agent_list = agent_list
        self.base_contract = random.sample(list(range(agent_list[0].n)), agent_list[0].n)
        self.contracts = [Contract(self.base_contract, None)]
        self.contracts[-1].add_agent_decision(True, 0)
        self.contracts.append(Contract(self.base_contract, self.contracts[-1]))
        self.contracts[-1].add_agent_decision(True, 0)
        self.max_contracts = max_contracts

        self.start_prob = start_prob
        self.end_prob = end_prob
        self.prob_step = prob_step
        self.prob_every_step = int(self.max_contracts * 1.1 / ((start_prob - end_prob) / prob_step))
        self.job_swaps = job_swaps

        self.current_prob = self.start_prob

        self.rounds = []
        self.costs_per_round = [[] for _ in range(len(agent_list)+1)]
        print(self.costs_per_round)

    def run_negotiation_process(self):
        """Executes a full negotiation with multiple rounds"""
        for n in range(0, self.max_contracts):
            self._round_of_negotiation(n)

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
        if round_n % self.prob_step == 0:
            self._adjust_temperature()

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
        """ Adjust temperature for all agents"""
        self.current_prob /= 2
        if self.current_prob <= 0:
            self.current_prob = self.end_prob
        print(f"\n🥵 Temperatures are cooling for probability {self.current_prob} 🥶")
        for agent in self.agent_list:
            agent.calc_temp(self.current_prob)
