The process of collecting traces is encompassing the following steps:

1- Running LTTng
Within our artifact, we create a channel consisting of eight buffers, each with a size of 64MB. This channel encompasses all system calls and events. Additionally, we incorporate contextual details like process name, PID, and TID into the events. The details of the tracing process are encapsulated within the "[tracing.sh](https://github.com/mnoferestibrocku/dataset-repo/blob/main/KernelTracing/tracing.sh)" script, which outlines the configurations and procedures for tracing.

2- Creating the Experiment Scenarios

Following figure gives an overview of the scenario used to create the system artifact. 
![image](https://github.com/mnoferestibrocku/dataset-repo/assets/131692985/5a332c24-baa0-48a9-b823-e9d345110a70)

To assess the system's performance, we define two separate workloads:
* Light-Load Scenario: This workload involves running two reports every 20 seconds. It is designed to simulate a situation with low processing demands, helping us evaluate the system's performance under minimal stress.
* Heavy-Load Scenario: In this workload, we generate 10 reports every 40 seconds. This aims to simulate a scenario with more data and higher computational demands, putting increased processing pressure on the system.

The irregular and undesired fluctuations in system behavior, known as performance noise, can impact the expected dependability of a system. To make the artifact more realistic and replicate real-world situations, we introduce four types of noise into the system. 
* CPU noise: The CPU noise is initiated  after 1200 seconds and lasts for 120 seconds. This noise simulates conditions of high CPU utilization or intensive processing activities which can affect the system performance. It is used to evaluate the system's capability to manage resource-intensive tasks and sustain  responsiveness under heavy CPU-intensive workloads.
* I/O noise: The I/O noise is activated at 1380 seconds and continues for 120 seconds. It emulates increased input/output (I/O) operations or data transfer activities that can potentially impact disk or storage performance. This noise enables the assessment of the system's performance when dealing with high I/O loads and its ability to handle data-intensive operations.
* Network noise: The network noise is introduced at 1560 seconds and persists for 120 seconds. It simulates network congestion, latency, or fluctuations in network connectivity, which can affect data transmission and communication between system components. By incorporating network noise, we can evaluate the system's resilience to network-related challenges and its ability to maintain effective data exchange under adverse network conditions.
* Memory noise: The memory noise is activated at 1740 seconds and lasts for 120 seconds. It represents increased memory usage or memory-related issues that can impact system performance and stability. This noise helps assess the system's ability to handle memory-intensive tasks and its responsiveness in memory-constrained situations.

3- Collecting Traces
Traces can be gathered using the "[tracing.sh](https://github.com/mnoferestibrocku/dataset-repo/blob/main/KernelTracing/tracing.sh)" script. When running the script, the first step prompts you to specify the output directory for collecting the traces. However, if you only intend to analyze the traces without capturing them, our pre-collected traces are available at the [Trace-RawData](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Trace-RawData) directory.

