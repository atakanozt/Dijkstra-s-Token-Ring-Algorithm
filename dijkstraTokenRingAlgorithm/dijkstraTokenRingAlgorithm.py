"""
Reference to the Dijkstra's paper:
https://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD426.html
"""
import random


def initialize_ring(n, k):
    """ Initialize a ring of n machines with random states from 0 to K-1. """
    return [random.randint(0, k - 1) for _ in range(n)]


def display_ring(ring):
    """ Helper function to display the ring's state. """
    print("Ring state:", ring)


def update_machine(ring, index, k):
    """ Update the state of the machine at the given index based on the K-state rules. """
    n = len(ring)
    left_neighbor = (index - 1) % n  # Handle wrap-around in the ring
    if index == 0:  # Bottom machine rule
        if ring[left_neighbor] == ring[index]:
            ring[index] = (ring[index] + 1) % k
            return True
    else:  # Other machines rule
        if ring[left_neighbor] != ring[index]:
            ring[index] = ring[left_neighbor]
            return True
    return False


def simulate_k_state_machines(n, k, steps=100):
    """ Simulate the ring of K-state machines for a given number of steps. """
    ring = initialize_ring(n, k)
    display_ring(ring)

    changes = True
    step = 0
    while changes and step < steps:
        changes = False
        for _ in range(n):  # Run through n random updates per step
            selected_machine = random.randint(0, n - 1)
            print(f"Selected machines : {selected_machine}")
            if update_machine(ring, selected_machine, k):
                changes = True
                print(f"Machine {selected_machine} has been updated.")
                display_ring(ring)

        step += 1

    print("Final state after", step, "steps:")
    display_ring(ring)


# Example usage
simulate_k_state_machines(n=5, k=6, steps=500)
