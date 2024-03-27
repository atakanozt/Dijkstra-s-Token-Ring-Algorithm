.. include:: substitutions.rst

|DistAlgName|
=========================================



Background and Related Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Efficient synchronization in concurrent computing is essential for the consistency and correctness of parallel applications. Barrier synchronization mechanisms are central to ensuring that all threads or processes in a shared memory system reach a predefined point in their execution before any can continue. Among various synchronization methods, the tournament barrier has emerged as a notable approach due to its structured and scalable nature.

**Tournament Barrier**

The tournament barrier utilizes a tree structure for organizing thread synchronization, drawing on the concept of tournament trees where processes compete in pairs. This method stands out for its predetermined matchups and hierarchical signaling process, which minimizes contention and scales effectively with the number of threads [Shavit1997]_.

**Related Work**

Several barrier synchronization techniques have been proposed, each with its own set of advantages and limitations:

- *Centralized barriers* suffer from scalability issues due to high contention with increasing thread counts.
- *Dissemination barriers* distribute synchronization in rounds, reducing contention but adding complexity.
- The *MCS (Mellor-Crummey and Scott) barrier* organizes threads in a tree structure, offering a balance between contention reduction and complexity [MellorCrummey1991]_.

The tournament barrier's approach to synchronization, predetermining matchups and employing a cascading wake-up process, offers a promising solution to the scalability and efficiency challenges faced by other barrier mechanisms. This study builds upon the foundational works by Mellor-Crummey and Scott, as well as Shavit and Touitou, to explore the nuances and performance implications of tournament barriers in high-concurrency environments.

.. [MellorCrummey1991] Mellor-Crummey, J. M., & Scott, M. L. (1991). "Algorithms for Scalable Synchronization on Shared-Memory Multiprocessors".



Distributed Algorithm: |DistAlgName|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An example distributed algorithm for implementing a tournament barrier on a shared memory system is presented in :ref:`Algorithm <TournamentBarrierAlgorithmLabel>`.

.. _TournamentBarrierAlgorithmLabel:

.. code-block:: RST
    :linenos:
    :caption: Tournament barrier algorithm.

    Implements: TournamentBarrier Instance: tb
    Uses: MemoryReadWrite, ThreadManagement
    Events: ReachBarrier, LeaveBarrier
    Needs:

    OnReachBarrier: (threadId) do
        round = 1
        while not isFinalRound(threadId, round) do
            opponentThreadId = findOpponent(threadId, round)
            if isWinner(threadId, opponentThreadId) then
                waitForOpponent(opponentThreadId)
            else
                signalWinner(opponentThreadId)
                waitUntilRoundComplete(round)
                exit
            end if
            round = round + 1
        done
        if isLastThread(threadId) then
            signalAllThreadsLeaveBarrier()
        else
            waitForSignalLeaveBarrier()
        end if

    OnLeaveBarrier: () do
        resetBarrierState()

The algorithm above outlines the tournament barrier mechanism, where threads synchronize at barrier points before proceeding. It operates on a simple principle: each thread is paired with another in a tournament-style matchup, where only one (the winner) proceeds to the next round. This process repeats until a final winner is determined, who then signals all threads to leave the barrier.

Explanation:

1. **Line 1-3:** Defines the algorithm, its instance, and dependencies.
2. **Line 5-6:** Event triggered when a thread reaches the barrier point.
3. **Line 7:** Initialization of the round counter.
4. **Line 8-20:** Main loop where each thread checks if it has reached the final round.
5. **Line 9-10:** Determining the opponent thread based on the current round and thread ID.
6. **Line 11-15:** The winner waits for the loser to signal completion, while the loser signals the winner and waits for the round to complete.
7. **Line 16-17:** Increment the round counter.
8. **Line 21-26:** The last thread signals all others to proceed, while others wait for this signal.
9. **Line 28-29:** Resets the state of the barrier once all threads have left.

Example
~~~~~~~

Consider a scenario with 8 threads reaching a synchronization point in a shared memory system. The threads are organized into a binary tree structure for the tournament, with each node representing a thread. In the first round, threads are paired (1 vs 2, 3 vs 4, etc.), with one thread from each pair proceeding to the next round after synchronization. This process continues until the final round, where the last remaining thread signals all threads to proceed past the barrier. This example demonstrates the efficiency of the tournament barrier in reducing contention and organizing thread synchronization in a scalable and structured manner.


Correctness
~~~~~~~~~~~

The tournament barrier algorithm ensures that no thread proceeds beyond the barrier until every thread has reached the barrier, maintaining the integrity of synchronized operations in shared memory systems.

**Safety**

The algorithm guarantees safety by preventing any thread from proceeding past the barrier until all threads have arrived. This is enforced through the tournament mechanism, where threads compete in pairs and only the winners advance. The ultimate winner, the last thread to win the tournament, signals all threads to proceed, ensuring no thread moves ahead prematurely.

.. code-block:: rst

    Safety is ensured as each thread must either win against its opponent or wait for a signal from its opponent, ensuring that no thread can bypass the barrier without all threads reaching it.

**Liveness**

Liveness is guaranteed as every thread that reaches the barrier will eventually be allowed to proceed. The algorithm's design, where each loser waits for a signal from its victorious opponent and the final winner signals all threads to continue, ensures no thread is indefinitely blocked.

.. code-block:: rst

    Liveness is achieved through a structured signaling mechanism, ensuring every waiting thread eventually receives a signal to proceed.

**Fairness**

The tournament barrier algorithm promotes fairness by ensuring that each thread has an equal opportunity to progress in the tournament structure. While the mechanism of winning and signaling is based on predefined matchups, every thread contributes to the synchronization process and will eventually pass the barrier.

.. code-block:: rst

    Fairness is inherent as each thread plays a role in the barrier's operation, either by winning and signaling or by waiting and then proceeding once signaled.

Complexity
~~~~~~~~~~

The theoretical complexity of the tournament barrier algorithm can be analyzed in terms of the number of messages and computational complexity.

**Number of Messages**

In a system with *n* threads, the total number of messages sent is proportional to *n-1*, corresponding to the number of matches in a complete binary tournament. Each match results in a signal being sent, either for synchronization (loser to winner) or for signaling completion (winner to all).

.. code-block:: rst

    The total number of messages is O(n), where n is the number of participating threads.

**Computational Complexity**

The computational complexity primarily revolves around the operations each thread performs to determine its opponent, win or lose a match, and signal other threads. Since these operations are executed once per round for a logarithmic number of rounds (log n), the overall computational complexity is O(log n).

.. code-block:: rst

    The computational complexity for each thread is O(log n), with n being the total number of threads.
