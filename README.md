# Enhancing Empirical Software Performance Engineering Research with Kernel-Level Events: A Comprehensive System Tracing Approach
This is the GitHub repository introduces an artifact contains kernel-level events gathered from Elasticsearch and Kibana. The IoT dataset serves as the data source, with 12 reports defined across two types of workloads: light and heavy, each running with different periods. Moreover, we enhance the artifact's realism by introducing four types of simulated noise—CPU, I/O, Network, and Memory—mimicking disruptions and challenges that impact performance and analysis accuracy. This repository contains all the system information, scripts, and guidlines required for reproducing the artifact. 

The raw trace data that we have collect is also placed in the repository. During the experiment, we collected both kernel events and system calls, resulting in a cumulative count of 24,263,691 events. We propose an artifact that serves three distinct applications. The first application emphasizes performance analysis by utilizing kernel events for monitoring. The second application targets noise detection and root cause analysis, again using kernel events. Finally, the third application investigates software phase detection through monitoring at the kernel level. These applications demonstrate that the proposed artifact assists researchers in evaluating system performance, robustness, and efficiency under disruptive 



# Performance Engineering
Performance engineering is a proactive and systematic approach aimed at designing, building, and enhancing software systems to ensure their efficient and reliable operation. It involves observing and measuring the operational behavior of a software system without interference, assessing performance metrics like response times, throughput, and resource utilization. This entails delving into kernel-level events related to performance monitoring, which play a significant role in understanding system behavior and diagnosing performance-related issues. Kernel-level events offer insights into how both the operating system and hardware resources are utilized. This information empowers system administrators, developers, and performance analysts to optimize and troubleshoot the system effectively.


 

# Kernel-level Events
We present an artifact that comprises kernel-level events collected through the utilization of well-known open-source tools, Elasticsearch and Kibana, renowned for their robust log management and analysis capabilities.

# Two Workloads
We defined reports thoughtfully organized into two distinct types of workloads: light and heavy. These workloads are executed at varying periods to provide you with a comprehensive range of scenarios. 

# Four Types of Noise
Our commitment to realism extends further as we introduce four types of simulated noise—CPU, I/O, Network, and Memory. 
These simulated noises replicate real-world disruptions and challenges, enhancing the authenticity of the artifact and offering a more accurate representation of performance and analysis accuracy challenges.

We invite you to explore, utilize, and contribute to this invaluable resource as we collectively work towards advancing performance engineering research and applications.
