# Noise Detection  Application of the Proposed Artifact
Performance analysis serves a dual purpose: it not only fine-tunes the utilization of system resources but also plays a crucial role in enhancing system reliability. The emergence of non-deterministic and undesired variations, referred to as performance noise, significantly impacts the anticipated or desired reliability of a system. This noise can lead to decreased throughput, heightened latency, inefficient resource utilization, and an overall decline in system performance.

Noises entail disruptions in performance that arise when a process encounters delays or interruptions while awaiting CPU or non-CPU resources like Disk I/O, Network I/O, or Memory. Observing kernel events can shed light on the characteristics of these noises and their underlying origins. Utilizing Trace Compase we wrote several script to visualize the Disk, Network, Interupt, and CPU noises.

## Step 1: Install Trace Compass and Import the Artifact
You can follow https://github.com/mnoferestibrocku/dataset-repo/blob/main/Applications/Performance-Monitoring/README.md for this step. 

## Step 2: Enable Javascript
For Javascript, the feature is available through the Tools -> Add-ons... under the Analyses category. You can search for the Trace Compass Scripting Javascript (Incubation) feature and click ``Finish``.
It will automatically install the required Trace Compass Scripting (Incubation) feature and all related features to edit and execute javascript with EASE.
After Trace Compass restart, the feature will be available.

## Step 3: Run the scripts
For each noise, a seprate scipt has been written. To execute, you should download and past it in the Trace Compass project. Then right click and select "Run As" and then "EASE Script". You can refer to this document for furthur information about Ease scripting (https://archive.eclipse.org/tracecompass.incubator/doc/org.eclipse.tracecompass.incubator.scripting.doc.user/User-Guide.html#Create_and_execute_a_script).

## Step 4: Noise Analysis
Figure~\ref{fig:main} provides a visual representation of the disk I/O-related metrics computed from the artifact, encompassing all 12 disks within the system. For a more detailed examination, one can zoom in on a specific time frame, as demonstrated in Figure~\ref{fig:subfig2}. This close-up view exposes a prolonged wait time for Disk 0. Such an observation prompts a comprehensive analysis to precisely identify the underlying origin of this noise. A deeper investigation into the extended wait duration for Disk 0 becomes crucial for the optimization of overall system performance and the assurance of dependable disk I/O operations.
