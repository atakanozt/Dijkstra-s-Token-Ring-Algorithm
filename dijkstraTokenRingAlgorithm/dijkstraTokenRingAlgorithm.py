"""
Simulation of K-State Machines in a Ring

This module simulates a ring of n machines, each of which can be in one of k states,
following specific update rules to explore state stabilization or patterns.

Reference:
- Dijkstra's EWD426: https://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD426.html
"""

import random

def initialize_ring(n, k):
    """
    Initializes a ring of n machines with random states from 0 to k-1.

    Args:
        n (int): Number of machines in the ring.
        k (int): Number of possible states each machine can be in.

    Returns:
        list: A list of integers representing the initial state of each machine.
    """
    return [random.randint(0, k - 1) for _ in range(n)]

def display_ring(ring):
    """
    Displays the current state of the ring.

    Args:
        ring (list): List of integers representing the state of each machine.
    """
    print("Ring state:", ring)

def update_machine(ring, index, k):
    """
    Updates the state of a machine at the given index based on the K-state rules.

    The rules are:
    - If it's the first machine (index 0), increment its state if it matches the state of
      its left neighbor, wrapping around with modulus k.
    - Other machines adopt the state of their left neighbor if they currently differ.

    Args:
        ring (list): List representing the ring of machines.
        index (int): Index of the machine to update.
        k (int): Total number of possible states.

    Returns:
        bool: True if the machine's state was changed, False otherwise.
    """
    n = len(ring)
    left_neighbor = (index - 1) % n  # Handle wrap-around in the ring
    if index == 0:  # Special rule for the first machine
        if ring[left_neighbor] == ring[index]:
            ring[index] = (ring[index] + 1) % k
            return True
    else:  # Standard rule for other machines
        if ring[left_neighbor] != ring[index]:
            ring[index] = ring[left_neighbor]
            return True
    return False

def simulate_k_state_machines(n, k, steps=100):
    """
    Simulates the ring of K-state machines for a given number of steps.

    Args:
        n (int): Number of machines in the ring.
        k (int): Number of possible states for each machine.
        steps (int): Maximum number of steps to simulate.

    The simulation randomly selects one machine per iteration to possibly update,
    displaying the state of the ring when changes occur.
    """
    ring = initialize_ring(n, k)
    display_ring(ring)

    changes = True
    step = 0
    while changes and step < steps:
        changes = False
        for _ in range(n):  # Run through n random updates per step
            selected_machine = random.randint(0, n - 1)
            if update_machine(ring, selected_machine, k):
                changes = True
                print(f"Machine {selected_machine} has been updated.")
                display_ring(ring)

        step += 1

    print("Final state after", step, "steps:")
    display_ring(ring)

