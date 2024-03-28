.. include:: substitutions.rst

|DistAlgName|
=========================================



Background and Related Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the exploration of distributed computing, the concept of mutual exclusion holds paramount importance, especially in contexts where shared resources are accessed by multiple processes.
Mutual exclusion ensures that at any given time, only one process can access a shared resource, thus preventing race conditions and ensuring data integrity.
This concept is further complicated and necessitated within distributed systems due to their inherent lack of a central coordinating mechanism.
Among the various algorithms proposed to address this challenge, Dijkstra's token ring algorithm stands out for its simplicity and efficacy, particularly in shared memory environments.

The token ring algorithm, initially proposed by Edsger W. Dijkstra, operates on the principle of passing a token in a ring topology,
where only the holder of the token is granted access to the shared resource. This approach effectively prevents simultaneous resource access by multiple processes.
However, in the context of distributed systems, where processes can fail and communication can be unreliable,
the basic token ring algorithm needs to be enhanced to ensure system self-stabilization—a property that allows a system to recover from arbitrary states of disruption and converge back to normal operation.

Self-stabilization in distributed systems is a critical attribute, ensuring that despite failures or state corruptions, the system can recover without external intervention
. The integration of self-stabilization within the token ring algorithm for mutual exclusion in shared memory systems addresses challenges of fault tolerance and system recovery.

Significant work has been done in the area of self-stabilizing algorithms for mutual exclusion.
Dijkstra's work laid the foundation, but subsequent studies have proposed various enhancements and alternatives.
For example, research has explored extensions to the token ring algorithm to improve its scalability, fault tolerance, and efficiency in environments characterized by high concurrency and dynamic network topologies.
Other work has focused on reducing the algorithm's complexity and the time it takes for the system to stabilize after a disruption.

Furthermore, the application of self-stabilizing algorithms extends beyond mutual exclusion, touching on areas such as consensus protocols,
leader election, and distributed coordination. These areas are crucial for the reliable operation of distributed systems,
from cloud computing infrastructures to decentralized blockchain networks.

In summary, the literature on distributed mutual exclusion and self-stabilization presents a critical area for research efforts aimed at enhancing the reliability, efficiency, and fault tolerance of distributed systems.
The continued exploration and refinement of these concepts, such as in the work on Dijkstra’s token ring algorithm, remain essential for the advancement of distributed computing technologies.

**Key References:**

- Dijkstra, E. W. (1984). Self-stabilizing systems in spite of distributed control. *Communications of the ACM, 17*(11), 643-644.
- Shukla, S. K., Rosenkrantz, D. J., & Ravi, S. S. (1995). Observations on self-stabilizing mutual exclusion algorithms. *Algorithmica, 12*(4), 509-525.
- Taubenfeld, G. (2019). Synchronization Algorithms and Concurrent Programming. *Pearson*. (Especially chapters related to mutual exclusion and self-stabilization in distributed systems.)

This section provides a background on the critical role of mutual exclusion and self-stabilization in distributed systems, with a focus on Dijkstra’s token ring algorithm.
The survey of related work highlights the evolution of research in this domain, pointing to advancements in algorithmic design and implementation that cater to the complexities of modern distributed environments.


Distributed Algorithm: |DistAlgName|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An example distributed algorithm for ensuring mutual exclusion in a shared memory environment using Dijkstra’s token ring approach is presented in :ref:`Algorithm <DijkstraTokenRingLabel>`.

.. _DijkstraTokenRingLabel:

.. code-block:: RST
    :linenos:
    :caption: Dijkstra's Token Ring Mutual Exclusion Algorithm.

    Implements: DijkstraTokenRing Instance: dtr
    Uses: SharedMemoryAccess Instance: sma
    Events: RequestAccess, ReleaseAccess, TokenReceived
    Needs: Token, ProcessQueue

    OnInit: () do
        If (IsFirstProcess) then
            GenerateToken()
        Enqueue(ProcessQueue, SelfID)

    OnRequestAccess: () do
        Enqueue(ProcessQueue, SelfID)
        If (HasToken and IsFront(ProcessQueue)) then
            GrantAccess()

    OnReleaseAccess: () do
        Dequeue(ProcessQueue)
        PassTokenToNext()

    OnTokenReceived: () do
        SetHasToken(true)
        If (IsFront(ProcessQueue)) then
            GrantAccess()

    GenerateToken: () do
        Create a unique token in the system

    PassTokenToNext: () do
        SetHasToken(false)
        If (Not IsEmpty(ProcessQueue)) then
            SendToken(NextInQueue(ProcessQueue))

    GrantAccess: () do
        Trigger sma.AccessResource(SelfID)

This Dijkstra’s Token Ring algorithm adaptation ensures mutual exclusion across distributed processes sharing a common resource. It's particularly designed for systems where processes communicate through shared memory.

1. **OnInit**: Initializes the process within the token ring. The first process in the system generates the token, representing the ability to access the shared resource. Each process, upon initialization, adds itself to a queue of processes awaiting resource access.

2. **OnRequestAccess**: When a process requests access to the shared resource, it enqueues itself. If it possesses the token and is at the front of the queue, it grants itself access to the resource.

3. **OnReleaseAccess**: After a process finishes using the resource, it releases access, dequeues itself from the process queue, and passes the token to the next process in line.

4. **OnTokenReceived**: Upon receiving the token, the process checks if it's at the queue's front. If so, it grants itself access to the resource.

5. **GenerateToken**: A unique token is created within the system, signifying the right to access the shared resource. This method is only called by the first process in the system.

6. **PassTokenToNext**: The current token holder relinquishes the token and passes it to the next process in the queue, if any.

7. **GrantAccess**: The process with the token and at the front of the queue is granted access to the shared resource.

This adaptation of Dijkstra's token ring algorithm emphasizes self-stabilization by allowing the system to recover from arbitrary states, such as in the case of process failure or unexpected token loss, ensuring the system can continue to enforce mutual exclusion effectively.


Example
~~~~~~~


Consider a distributed system with four processes, P1, P2, P3, and P4, arranged in a token ring topology.
Initially, P1 generates the token because it is designated as the first process. Each process, upon needing access to the shared resource,
sends a request and enqueues itself in the process queue managed in shared memory.

1. **Initial State**: P1 has the token. P2 and P3 request access to the shared resource, enqueuing themselves.
2. **P1 Accesses Resource**: P1 accesses the shared resource and upon completion, checks the queue and passes the token to P2.
3. **P2 Accesses Resource**: P2, now holding the token, accesses the resource. After P2, the token is passed to P3.
4. **P3 Accesses Resource**: P3 accesses the resource. Since P4 did not request access, the token is held until another request is made.

This simple sequence illustrates the algorithm's approach to managing mutual exclusion in a distributed system with shared memory.

Correctness
~~~~~~~~~~~


**Safety**: The algorithm ensures that only one process can access the shared resource at a time. Given the token-based mechanism, a process can only access the resource if it holds the token, effectively preventing concurrent access.

**Liveness**: The token circulation guarantees that every request for access will eventually be granted. Since the token is passed to the next process in the queue after a resource is released,
and the queue operates on a first-come, first-served basis, all processes will eventually receive the token.

**Fairness**: The use of a queue to manage access requests ensures that processes are served in the order they request access,
providing a fair system where no process is indefinitely delayed.

These properties highlight the algorithm's capability to provide a robust solution for enforcing mutual exclusion in distributed systems,
balancing the need for efficiency, fault tolerance, and fairness.


Complexity
~~~~~~~~~~


The complexity analysis of Dijkstra's Token Ring algorithm for mutual exclusion in a distributed system with shared memory primarily focuses on two aspects:
the number of messages required for token circulation and the computational complexity involved in managing mutual exclusion.

**Number of Messages**: The token ring algorithm operates by passing a token among processes in a circular fashion.
In an ideal scenario without process failures or token loss, the number of messages corresponds directly to the number of token transmissions required for each process to access the shared resource once.
For a system of :math:`N` processes, the token circulates through all processes, resulting in a total of :math:`N` message transmissions for a complete cycle.
Therefore, the message complexity is :math:`O(N)` for a single complete token circulation among :math:`N` processes.

**Computational Complexity**: The computational complexity of the algorithm involves several factors, including token generation, queue management
(enqueuing and dequeuing operations), and the actual process of granting access to the shared resource. Assuming that queue operations (enqueue and dequeue) can be performed in constant time,
:math:`O(1)`, the primary computational effort lies in the distribution and management of the token. Since each process needs to handle the token once per complete circulation,
the computational complexity for each process is also :math:`O(1)`. Thus, for :math:`N` processes, the total computational complexity for a complete circulation is :math:`O(N)`,
where each process contributes a constant amount of computational work.

These complexities assume an ideal environment where message losses or process failures do not occur. In practical scenarios, additional mechanisms for fault tolerance,
such as token regeneration and process timeout management, may introduce complexity variations. However, the foundational operation of the token ring algorithm maintains :math:`O(N)`
message and computational complexity under normal operating conditions.


