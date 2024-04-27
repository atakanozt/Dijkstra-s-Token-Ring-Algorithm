import math
import time
from adhoccomputing.GenericModel import GenericModel

class TournamentBarrierComponent(GenericModel):
    """
    Represents a single participant in a tournament barrier synchronization algorithm.
    Each component can notify its opponent in the tournament structure.

    Attributes:
        coordinator (TournamentBarrierCoordinator): The coordinator managing the tournament.
        previous_opponents (list): A list of opponent IDs that this node has faced.
    """
    def __init__(self, componentname, componentid, coordinator, topology=None):
        super().__init__(componentname, componentid, topology=topology)
        self.coordinator = coordinator
        self.previous_opponents = []  # Initialize the list to track opponents
        self.coordinator.register_node(self, componentid)

    def notify_opponent(self, round):
        """
        Notifies the opponent from a previous round to wake up, simulating the synchronization mechanism.

        Args:
            round (int): The current round in the tournament from which the opponent will be notified.
        """
        if round < len(self.previous_opponents):
            opponent_id = self.previous_opponents[round]
            print(f"Node {self.componentinstancenumber} waking up Node {opponent_id} from round {round + 1}")
            self.coordinator.nodes[opponent_id].notify_opponent(round + 1)
            self.coordinator.increment_message_count()

class TournamentBarrierCoordinator(GenericModel):
    """
    Coordinates the entire tournament barrier synchronization process among all participating nodes.

    Attributes:
        num_participants (int): Total number of participants in the barrier.
        nodes (dict): Dictionary of node instances.
        active_nodes (list): List of IDs for nodes currently active in the current round.
        current_round (int): The current round in the tournament.
        max_rounds (int): Maximum number of rounds in the tournament, calculated from the number of participants.
        message_count (int): Counter for the total messages sent for synchronization purposes.
        start_time (float): Timestamp when the tournament starts.
        end_time (float): Timestamp when the tournament ends.
    """
    def __init__(self, componentname, componentid, num_participants, topology=None):
        super().__init__(componentname, componentid, topology=topology)
        self.num_participants = num_participants
        self.nodes = {}
        self.active_nodes = list(range(num_participants))
        self.current_round = 0
        self.max_rounds = int(math.ceil(math.log2(num_participants)))
        self.message_count = 0
        self.start_time = time.time()
        self.end_time = 0

    def increment_message_count(self):
        """
        Increments the count of messages sent during the tournament.
        """
        self.message_count += 1

    def register_node(self, node, node_id):
        """
        Registers a node in the coordinator's node dictionary.

        Args:
            node (TournamentBarrierComponent): The node to register.
            node_id (int): The identifier for the node.
        """
        self.nodes[node_id] = node

    def advance_round(self):
        """
        Advances the tournament to the next round, updating active nodes based on match results.
        """
        if self.current_round < self.max_rounds:
            print(f"Advancing to round {self.current_round + 1}")
            next_round_nodes = []
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
                print(f"Final winner is Node {self.active_nodes[0]}")
                self.nodes[self.active_nodes[0]].notify_opponent(self.current_round - 1)
                self.end_time = time.time()

    def simulate_match(self, id1, id2):
        """
        Simulates a match between two nodes, determining the winner based on a predefined logic.

        Args:
            id1 (int): The ID of the first node.
            id2 (int): The ID of the second node.

        Returns:
            int: The ID of the winning node.
        """
        winner = id1 if id1 < id2 else id2
        self.increment_message_count()
        print(f"Match between Node {id1} and Node {id2}, Winner: Node {winner}")
        return winner

    def notify_next_round(self, node_id):
        """
        Initiates the notification process for the next round, calling on nodes to wake their opponents.

        Args:
            node_id (int): The ID of the node that will start the notification.
        """
        self.nodes[node_id].notify_opponent(self.current_round - 1)

