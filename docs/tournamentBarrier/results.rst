.. include:: substitutions.rst

Implementation, Results and Discussion
======================================

Implementation and Methodology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The implementation of the tournament barrier algorithm within a parallel computing environment adheres to the scientific method's principle of verifiability. Our approach ensures that other researchers can replicate our experiment to verify the results, underpinning the validity of our findings. This section details the equipment and techniques used, offering a comprehensive insight into the methodology applied [Shuttleworth2016]_.

**Materials and Equipment**: The experiment was conducted using a simulated parallel computing environment on the AHCv2 platform. This environment is designed to mimic a multicore processor architecture, facilitating the execution of concurrent threads and the implementation of synchronization mechanisms like the tournament barrier.

**Sample Gathering and Preparation**: Threads were programmatically generated within the AHCv2 environment, simulating a typical use case in a shared memory system. Each thread was assigned a unique identifier and tasked with executing a predefined set of operations, reaching the synchronization point at varying times to test the barrier's effectiveness.

**Measurements and Calculations**: The primary measurements included synchronization time—the time taken for all threads to pass through the barrier—and system overhead introduced by the barrier synchronization process. These metrics were calculated using timestamps captured at key execution points, with the raw data processed to determine average synchronization times and overhead.

**Statistical Techniques**: Analysis of the data involved statistical methods to evaluate the performance and efficiency of the tournament barrier algorithm. Techniques included mean calculation, variance analysis, and comparison with other barrier synchronization mechanisms to assess relative performance [Shuttleworth2016]_.

Results
~~~~~~~

This code has not been tested and implemented fully yet.

Discussion
~~~~~~~~~~

This part cannot be discussed for now.

.. [Shuttleworth2016] M. Shuttleworth. (2016) Writing methodology. `Online <https://explorable.com/writing-methodology>`_.
