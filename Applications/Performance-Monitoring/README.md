# A method commonly employed to assess the performance of multi-threaded applications revolves around the examination of the critical path. 
# The critical path provides a visual representation of instances when a request encountered delays or was obstructed. Such paths prove invaluable for uncovering the origins and reasons behind latency occurrences.
# This application utilizes the algorithm provided by the open-source trace analysis software \textit{Trace Compass 8.2.0} \footnote{URL: https://wiki.eclipse.org/Trace\_Compass/Development\_Environment\_Setup} to compute the critical paths of the relevant threads.
# You can follow the steps towards this application:

# Step 1: Trace Compass Installation
## The tutorial found at https://wiki.eclipse.org/Trace_Compass/Development_Environment_Setup do a good job of explaining how to install Trace Compass.

# Step 2: Import Traces
## In Trace Compass: 1. Click Window, then Show View. Type in "Project Explorer", click Project Explorer in the list, then click Open. 
## 2. Right click in the Project Explorer window, hover over New, then select Project. 
## 3. Make sure Tracing > Tracing Project is selected, then click Next. 
## 4. Type in "Trace Compass Project" into the Project name: text input, then click Finish. 
## 5. Right click your project in the Project Explorer window, then click Import. 
## 6. Make sure General > File System is selected, then click Next. 
## 7. Click Browse, then navigate to the Trace Compass Project folder in the supplied Artifact directory, and click Open. 
## 8. Check Trace Compass Project and click Finish. 
## 9. Right click on Traces, and click Import. 
## 10. Click Browse, then navigate to the Traces folder in the supplied Artifact directory, and click Open. 
## 11. Check Traces and click Finish. Everything is now set up.

# Step 3: Critical Path Analysis
## In "Control Flow" view, search for elasticsearch process, then right click  and select option "Follow"
## In "Critical Path" view, you can see the critical path of the elasticsearch process, which is existed in directory as . 
