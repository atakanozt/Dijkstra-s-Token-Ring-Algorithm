import math
from adhoccomputing.GenericModel import GenericModel


class TournamentBarrierComponent(GenericModel):
    def __init__(self, componentname, componentid, coordinator, topology=None):
        super().__init__(componentname, componentid, topology=topology)
        self.coordinator = coordinator
        self.previous_opponents = []  # Initialize the list to track opponents
        self.coordinator.register_node(self, componentid)

    def notify_opponent(self, round):
        if round < len(self.previous_opponents):
            opponent_id = self.previous_opponents[round]
            print(f"Node {self.componentinstancenumber} waking up Node {opponent_id} from round {round + 1}")
            self.coordinator.nodes[opponent_id].notify_opponent(round + 1)


class TournamentBarrierCoordinator(GenericModel):
    def __init__(self, componentname, componentid, num_participants, topology=None):
        super().__init__(componentname, componentid, topology=topology)
        self.num_participants = num_participants
        self.nodes = {}
        self.active_nodes = list(range(num_participants))  # Initialize active nodes as a list
        self.current_round = 0
        self.max_rounds = int(math.ceil(math.log2(num_participants)))

    def register_node(self, node, node_id):
        self.nodes[node_id] = node

    def advance_round(self):
        if self.current_round < self.max_rounds:
            print(f"Advancing to round {self.current_round + 1}")
            next_round_nodes = []
            # Make pairs from the current list of active nodes
            i = 0
            while i < len(self.active_nodes) - 1:
                id1 = self.active_nodes[i]
                id2 = self.active_nodes[i + 1]
                winner_id = self.simulate_match(id1, id2)
                next_round_nodes.append(winner_id)
                i += 2
            self.active_nodes = next_round_nodes
            self.current_round += 1
            print(f"Active nodes for round {self.current_round}: {self.active_nodes}")
            if len(self.active_nodes) == 1 and self.current_round == self.max_rounds:
                # Only one node left, final winner
                print(f"Final winner is Node {self.active_nodes[0]}")
                self.nodes[self.active_nodes[0]].notify_opponent(self.current_round - 1)

    def simulate_match(self, id1, id2):
        winner = id1 if id1 < id2 else id2
        print(f"Match between Node {id1} and Node {id2}, Winner: Node {winner}")
        return winner

    def notify_next_round(self, node_id):
        # Start the backtracking process of waking up
        self.nodes[node_id].notify_opponent(self.current_round - 1)
