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
-------

.. note::
   I have some plots to show and inform you about, but I couldn't include them in this PDF. Therefore, I will present those graphs and plots during the presentation. Thank you for your understanding.


The tournament barrier study employed a robust, simulation-based approach on a distributed computing platform to explore the algorithm's efficacy and efficiency in thread synchronization. This setup allowed for the rigorous assessment of synchronization mechanisms under varied conditions and loads.

1. **Research Methodology Used**:
   The study used an experimental simulation methodology, which involved emulating a concurrent computing environment on a distributed system to assess the tournament barrier's synchronization efficiency.

2. **Originality of the Study**:
   This was an original study that specifically focused on the tournament barrier—a less commonly applied but potentially more efficient barrier synchronization mechanism compared to traditional methods.

3. **Measurement Tools**:
   Custom-built software tools and logging mechanisms were utilized to measure synchronization times, message passing efficiency, and overall system performance during the synchronization process.

4. **Procedure Structure and Implementation**:
   The procedures were meticulously structured, with simulations designed to replicate varying loads and synchronization scenarios. Each thread or node represented a process participating in the tournament-style barrier synchronization.

5. **Extent of Experimentations**:
   Extensive experimentations were conducted to ensure robust and statistically significant results. These included repeated trials at each level of system load to provide not only mean values but also confidence intervals, ensuring the reliability of the findings.

6. **Assessed Parameters and Their Adequacy**:
   The primary parameters assessed were synchronization time, number of messages passed, and latency in message delivery. These parameters are crucial for evaluating the efficiency of any barrier synchronization mechanism and were found to be adequate for this study.


Discussion
----------

The results from the tournament barrier study provide valuable insights into its operational effectiveness and potential applications in complex, highly concurrent systems. Key discussion points include:

- **Efficiency in Synchronization**: The tournament barrier demonstrated high efficiency in reducing synchronization times compared to more traditional barriers, making it suitable for systems where rapid synchronization is crucial.

- **Scalability**: The structured matchups and predetermined progression through rounds help in maintaining performance even as the number of concurrent threads increases, highlighting the barrier’s scalability.

- **Resource Utilization**: Despite its efficiency, the tournament barrier may require more initial setup and resource allocation (in terms of setting up the tree structure and managing node progressions), which could be a consideration for systems with limited resources.

- **Potential Applications**: Given its characteristics, the tournament barrier could be particularly beneficial in environments that require frequent and reliable synchronization among many concurrent processes, such as high-performance computing and real-time data processing systems.

The study underscores the importance of selecting an appropriate synchronization mechanism tailored to the specific needs of the system, with the tournament barrier offering a promising alternative for complex scenarios.

.. note::
   Future studies could explore hybrid models that combine the tournament barrier with other synchronization mechanisms to enhance efficiency and adaptability across various computing environments.

.. [Shuttleworth2016] M. Shuttleworth. (2016) Writing methodology. `Online <https://explorable.com/writing-methodology>`_.
