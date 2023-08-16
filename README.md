# Enhancing Empirical Software Performance Engineering Research with Kernel-Level Events: A Comprehensive System Tracing Approach
Welcome to our GitHub repository, where we present an artifact housing kernel-level events extracted from Elasticsearch and Kibana. Powered by the IoT dataset, this artifact comprises 12 reports categorized into light and heavy workloads, each running with varying intervals. We've added a touch of realism by incorporating four simulated noise types—CPU, I/O, Network, and Memory—to emulate real-world disruptions that affect performance and analysis precision. This repository serves as a comprehensive resource, providing all necessary system information, scripts, and guidelines to effortlessly reproduce the artifact.

The repository also contains the raw trace data we've collected. Throughout the experiment, we gathered a total of 24,263,691 events by capturing both kernel events and system calls. Our artifact introduces three distinct applications. The first focuses on performance analysis, utilizing kernel events for effective monitoring. The second application is dedicated to noise detection and root cause analysis, leveraging kernel events once again. Lastly, the third application explores software phase detection through kernel-level monitoring. These applications showcase the artifact's ability to aid researchers in assessing system performance, resilience, and efficiency, especially in the face of disruptive conditions.


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
