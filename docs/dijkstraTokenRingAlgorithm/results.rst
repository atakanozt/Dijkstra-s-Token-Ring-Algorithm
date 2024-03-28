.. include:: substitutions.rst

Implementation and Methodology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Implementation Details:**

The implementation of Dijkstra's Token Ring algorithm for mutual exclusion was conducted on the Advanced High-performance Computing Version 2 (AHCv2) platform,
a distributed computing environment designed to simulate distributed systems operations. The platform allows for the emulation of multiple nodes (processes) communicating over a shared memory architecture,
closely mimicking real-world distributed systems.


**Methodology:**

1. **Sample Gathering and Preparation**: The distributed system was emulated with varying numbers of nodes (processes), ranging from 4 to 16, to analyze the algorithm's performance under different scales.
Each node represents a process in the Dijkstra's Token Ring algorithm.

2. **Randomization Techniques**: To simulate real-world operating conditions, node failures and network latencies were introduced randomly across the experiments.
This approach ensures a robust test of the algorithm's fault tolerance and self-stabilization capabilities.

3. **Measurements and Calculations**: The primary measurements included the time taken for token circulation, the number of messages transmitted, and the system's stabilization time following a disruption (e.g., node failure).
These measurements were taken using high-resolution system clocks and logged for analysis.


**Results and Discussion:**

The results obtained from the implementation are discussed in detail in the following sections, highlighting the algorithm's performance under various conditions, its scalability, and its fault tolerance capabilities.
A critical analysis of the results provides insights into the algorithm's practical applications and potential areas for improvement.


Results
~~~~~~~~

This code has not been fully implemented and tested yet.

Discussion
~~~~~~~~~~

Since we haven't tested this algorithm, we cannot discuss for now.


