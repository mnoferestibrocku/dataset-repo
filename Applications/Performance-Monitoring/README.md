# Performance Monitoring Application of the Proposed Artifact
A method commonly employed to assess the performance of multi-threaded applications revolves around the examination of the critical path. 
The critical path provides a visual representation of instances when a request encountered delays or was obstructed. Such paths prove invaluable for uncovering the origins and reasons behind latency occurrences.
This application utilizes the algorithm provided by the open-source trace analysis software Trace Compass 8.2.0 to compute the critical paths of the relevant threads. You can follow the steps towards this application:

## Step 1: Trace Compass Installation
The tutorial found at https://wiki.eclipse.org/Trace_Compass/Development_Environment_Setup do a good job of explaining how to install Trace Compass.

## Step 2: Import Traces
In Trace Compass: 1. Click Window, then Show View. Type in "Project Explorer", click Project Explorer in the list, then click Open. 
2. Right click in the Project Explorer window, hover over New, then select Project. 
3. Make sure Tracing > Tracing Project is selected, then click Next. 
4. Type in "Trace Compass Project" into the Project name: text input, then click Finish. 
5. Right click your project in the Project Explorer window, then click Import. 
6. Make sure General > File System is selected, then click Next. 
7. Click Browse, then navigate to the Trace Compass Project folder in the supplied Artifact directory, and click Open. 
8. Check Trace Compass Project and click Finish. 
9. Right click on Traces, and click Import. 
10. Click Browse, then navigate to the Traces folder in the supplied Artifact directory, and click Open. 
11. Check Traces and click Finish. Everything is now set up.

## Step 3: Critical Path Analysis
In "Control Flow" view, search for elasticsearch process, then right click  and select option "Follow"
In "Critical Path" view, you can see the critical path of the elasticsearch process, which is existed in directory as CriticalPath.png. 

## Step 4: Block Event Analysis
In  CriticalPath.png, a distinct block period comes to the fore, illustrating a phase during which Elasticsearch encounters disk-related blocking. This interval is accompanied by a sequence of different events showcased in EventsDuringBlockDuration.png which shows the event view of Trace Compass. Among these events, there's a sequence involving sched_switch occurrences, followed by futex and IRQ events, culminating in the appearance of the block_rq_complete event. This latter event signifies the completion of the blocked request, allowing the process to regain access to the CPU. Researchers often utilize these events to gauge scheduling efficiency. Leveraging this artifact, they can assess these aspects based on the behavior of Elasticsearch under various workloads, as demonstrated by this artifact.

## Step 5: I/O Throughput Analysis
Furthermore, in IOReadWriteThroughput.png which shows the "Disk I/O Activity" view of Trace Compass, the read and write throughput of the Disk is showcased through the time interval spanning from the receipt of a request block_rq_issue to its completion block_rq_complete. Although fluctuations in disk throughput are evident, it becomes apparent that the presence of noise significantly influences disk usage, leading to heightened utilization.
