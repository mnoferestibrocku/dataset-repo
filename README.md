# Enhancing Empirical Software Performance Engineering Research with Kernel-Level Events: A Comprehensive System Tracing Approach
Welcome to our GitHub repository, where we present an artifact housing kernel-level events extracted from Elasticsearch and Kibana. Powered by the IoT dataset, this artifact comprises 12 reports categorized into light and heavy workloads, each running with varying intervals. We've added a touch of realism by incorporating four simulated noise types—CPU, I/O, Network, and Memory—to emulate real-world disruptions that affect performance and analysis precision. This repository serves as a comprehensive resource, providing all necessary system information, scripts, and guidelines to effortlessly reproduce the artifact.

The repository also contains the raw trace data we've collected. Throughout the experiment, we gathered a total of 24,263,691 events by capturing both kernel events and system calls. Our artifact introduces three distinct applications. The first focuses on performance analysis, utilizing kernel events for effective monitoring. The second application is dedicated to noise detection and root cause analysis, leveraging kernel events once again. Lastly, the third application explores software phase detection through kernel-level monitoring. These applications showcase the artifact's ability to aid researchers in assessing system performance, resilience, and efficiency, especially in the face of disruptive conditions.

# Experiment Setup
To generate the artifact, you need a fresh installation of "Linux Ubuntu 22.04.2 LTS," which should include default applications and be free from any third-party software installations. Following this, the artifact requires a series of steps to set up the essential tools:
 
* Step 1: Install LTTNG
* Step 2: Install Java
* Step 3: Install Elasticsearch and Kibana
* Step 4: Download and Import Dataset into Elasticsearch
* Step 5: Create Workloads
* Step 6: Install stress-ng

Follow these straightforward instructions to establish the necessary tools and prepare your environment for further exploration. The scripts and workloads are detailed in the "[Installation](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Installation)" directory.

While you can run the experiment in any environment, it's worth noting that the provided dataset was generated on a machine with specifications outlined in the "[system-info.txt](https://github.com/mnoferestibrocku/dataset-repo/blob/main/system-info.txt)" file.

# Kernel Tracing
To capture these events, we employ LTTng (Linux Tracing Toolkit: next generation), an open-source tracing tool. LTTng is renowned for its minimal overhead and scalability, making it suitable for tracing both the Linux kernel and user space applications. Each trace event is characterized by attributes such as Timestamp, CPU, event type (e.g., system call, interrupt), event details (e.g., IP address), process ID (PID), and thread ID (TID). To gather these essential attributes, LTTng utilizes tracepoints, strategically positioned hooks within the code that permit function probes to attach during runtime.

The collection of traces is detailed in the "[KernelTracing](https://github.com/mnoferestibrocku/dataset-repo/tree/main/KernelTracing)" directory, which includes:
   - Step 1: Running LTTng
   - Step 2: Building the Experiment Scenarios
   - Step 3: Collecting Traces

In our artifact, we establish a channel composed of eight buffers, each boasting a size of 64MB. All system calls and events are enabled within this channel. Furthermore, we include context information including process name, PID, and TID to the events. The specifics of tracing are encapsulated in the "[tracing.sh](https://github.com/mnoferestibrocku/dataset-repo/blob/main/KernelTracing)" directory, which outlines the tracing configurations and procedures.


# Artifact Applications
 
We present three separate applications that showcase the use-ability of our proposed artifact. 
* Performance Monitoring: The first application focuses on performance analysis, highlighting the effective monitoring of system performance using kernel events. Detailed descriptions and relevant figures for this application are available in the "[Applications/Performance-Monitoring](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Applications/Performance-Monitoring)" directory.
* Noise Detection: The second application emphasizes noise detection and in-depth root cause analysis through the utilization of kernel events. You can find descriptions, implementation scripts, and relevant figures related to this application in the "[Applications/Noise-Detection](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Applications/Noise-Detection)" directory.
* Software Phase Detection: Our artifact also serves the purpose of software phase detection by leveraging the monitoring of kernel-level events. Each of these applications underscores a unique capability of our artifact within the realm of performance engineering research. To delve into further details about this particular application, including descriptions, and relevant scripts, please refer to the "[Applications/Phase-Detection](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Applications/Phase-Detection)" directory..


# Conclusion

This enriched artifact empowers researchers to assess system performance, resilience, and effectiveness when faced with disruptive scenarios. Through its utilization, valuable insights can be obtained for enhancing system performance, recognizing vulnerabilities, and formulating effective strategies to counter the effects of disruptions.

