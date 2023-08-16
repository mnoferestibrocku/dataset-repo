# Enhancing Empirical Software Performance Engineering Research with Kernel-Level Events: A Comprehensive System Tracing Approach
Welcome to our GitHub repository, where we present an artifact housing kernel-level events extracted from Elasticsearch and Kibana. Powered by the IoT dataset, this artifact comprises 12 reports categorized into light and heavy workloads, each running with varying intervals. We've added a touch of realism by incorporating four simulated noise types—CPU, I/O, Network, and Memory—to emulate real-world disruptions that affect performance and analysis precision. This repository serves as a comprehensive resource, providing all necessary system information, scripts, and guidelines to effortlessly reproduce the artifact.

The repository also contains the raw trace data we've collected. Throughout the experiment, we gathered a total of 24,263,691 events by capturing both kernel events and system calls. Our artifact introduces three distinct applications. The first focuses on performance analysis, utilizing kernel events for effective monitoring. The second application is dedicated to noise detection and root cause analysis, leveraging kernel events once again. Lastly, the third application explores software phase detection through kernel-level monitoring. These applications showcase the artifact's ability to aid researchers in assessing system performance, resilience, and efficiency, especially in the face of disruptive conditions.

# Experiment Setup

# Kernel Tracing

# Experiment Scenario
Following figure gives an overview of the scenario used to create the system artifact. 
![image](https://github.com/mnoferestibrocku/dataset-repo/assets/131692985/5a332c24-baa0-48a9-b823-e9d345110a70)

To assess the system's performance, we define two separate workloads:
* Light-Load Scenario: This workload involves running two reports every 20 seconds. It is designed to simulate a situation with low processing demands, helping us evaluate the system's performance under minimal stress.
* Heavy-Load Scenario: In this workload, we generate 10 reports every 40 seconds. This aims to simulate a scenario with more data and higher computational demands, putting increased processing pressure on the system.

The irregular and undesired fluctuations in system behavior, known as performance noise, can impact the expected dependability of a system. To make the artifact more realistic and replicate real-world situations, we introduce four types of noise into the system. 
* CPU noise: The CPU noise is initiated  after 1200 seconds and lasts for 120 seconds (as shown in Figure~\ref{fig:artifactscenario}). This noise simulates conditions of high CPU utilization or intensive processing activities which can affect the system performance. It is used to evaluate the system's capability to manage resource-intensive tasks and sustain  responsiveness under heavy CPU-intensive workloads.
* I/O noise: The I/O noise is activated at 1380 seconds and continues for 120 seconds. It emulates increased input/output (I/O) operations or data transfer activities that can potentially impact disk or storage performance. This noise enables the assessment of the system's performance when dealing with high I/O loads and its ability to handle data-intensive operations.
* Network noise: The network noise is introduced at 1560 seconds and persists for 120 seconds. It simulates network congestion, latency, or fluctuations in network connectivity, which can affect data transmission and communication between system components. By incorporating network noise, we can evaluate the system's resilience to network-related challenges and its ability to maintain effective data exchange under adverse network conditions.
* Memory noise: The memory noise is activated at 1740 seconds and lasts for 120 seconds. It represents increased memory usage or memory-related issues that can impact system performance and stability. This noise helps assess the system's ability to handle memory-intensive tasks and its responsiveness in memory-constrained situations.

# Artifact Applications
 
We present three separate applications that showcase the use-ability of our proposed artifact. 
* Performance Monitoring: The first application focuses on performance analysis, highlighting the effective monitoring of system performance using kernel events. Detailed descriptions and relevant figures for this application are available in the "[Applications/Performance-Monitoring](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Applications/Performance-Monitoring)" directory.
* Noise Detection: The second application emphasizes noise detection and in-depth root cause analysis through the utilization of kernel events. You can find descriptions, implementation scripts, and relevant figures related to this application in the "[Applications/Noise-Detection](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Applications/Noise-Detection)" directory.
* Software Phase Detection: Lastly, our artifact finds application in software phase detection through the monitoring of kernel-level events. Each of these applications highlights a distinct capability of our artifact within the domain of performance engineering research topics. You can find descriptions, implementation scripts, and relevant figures related to this application in the "[Applications/Noise-Detection](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Applications/Phase-Detection)" directory.


# Conclusion

This enriched artifact empowers researchers to assess system performance, resilience, and effectiveness when faced with disruptive scenarios. Through its utilization, valuable insights can be obtained for enhancing system performance, recognizing vulnerabilities, and formulating effective strategies to counter the effects of disruptions.

