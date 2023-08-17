The process of collecting traces is encompassing the following steps:

# Step 1: Running LTTng

Within our artifact, we create a channel consisting of eight buffers, each with a size of 64MB. This channel encompasses all system calls and events. Additionally, we incorporate contextual details like process name, PID, and TID into the events. The details of the tracing process are encapsulated within the "[tracing.sh](https://github.com/mnoferestibrocku/dataset-repo/blob/main/KernelTracing/tracing.sh)" script, which outlines the configurations and procedures for tracing.

# Step 2: Creating the Experiment Scenarios

Following figure gives an overview of the scenario used to create the system artifact. 
![image](https://github.com/mnoferestibrocku/dataset-repo/assets/131692985/5a332c24-baa0-48a9-b823-e9d345110a70)

To assess the system's performance, we define two separate workloads:
* Light-Load Scenario: This workload involves running two reports every 20 seconds.
  > curl -XPOST "http://localhost:9200/_watcher/watch/lightloadid/_start"
* Heavy-Load Scenario: In this workload, we generate 10 reports every 40 seconds.
  > curl -XPOST "http://localhost:9200/_watcher/watch/highloadid/_start"

To make the artifact more realistic and replicate real-world situations, we introduce four types of noise into the system. 
* CPU noise: The CPU noise is initiated  after 1200 seconds and lasts for 120 seconds. We initiate the stress-ng tool to create CPU noise by performing matrix multiplication with a matrix size of 256x256 with 6 workers for a duration of 120 seconds.
  > stress-ng --matrix 6 --matrix-method prod --matrix-size 256 --timeout 120
  
* I/O noise: The I/O noise is activated at 1380 seconds and continues for 120 seconds. For I/O noise, we trigger the stress-ng tool to generate I/O stress by employing a mix of different I/O operations with 6 concurrent workers for a duration of 120 seconds.
  > stress-ng --iomix 6 --timeout 120

* Network noise: The network noise is introduced at 1560 seconds and persists for 120 seconds. INetwork noise is introduced using 6 workers that engage in various socket stress activities. This includes pairs of client/server processes executing rapid connect, send, and receive operations, as well as disconnects on the local host.
  > stress-ng --sock 6 --timeout 120

* Memory noise: The memory noise is activated at 1740 seconds and lasts for 120 seconds. The generation of memory noise entails allocating 4GB per each set of 6 workers, who continually call mmap/munmap and write to the allocated memory.
  > stress-ng --vm 6 --vm-bytes 4G --timeout 120

# Step 3: Collecting Traces
Traces can be gathered using the "[tracing.sh](https://github.com/mnoferestibrocku/dataset-repo/blob/main/KernelTracing/tracing.sh)" script. When running the script, the first step prompts you to specify the output directory for collecting the traces. However, if you only intend to analyze the traces without capturing them, our pre-collected traces are available at the [Trace-RawData](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Trace-RawData) directory.

