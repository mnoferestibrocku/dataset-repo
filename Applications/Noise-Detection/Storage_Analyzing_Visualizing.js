// Load the proper modules
loadModule("/TraceCompass/Trace")
loadModule("/TraceCompass/Analysis")
loadModule("/TraceCompass/DataProvider")
loadModule("/TraceCompass/View")

// Get the active trace
var trace = getActiveTrace()

// Get an event iterator on that trace
var iter = getEventIterator(trace)

//Create an analysis
var analysis = createScriptedAnalysis(trace, 'Disk Noise');

// Get the analysis's state system so we can fill it
var ss = analysis.getStateSystem(false);

//counter and current reads initalization.
interval = [];
countInsert = 0;
countIssue = 0;
countComplete = 0;
currReads = 0;
countAVG = 0;
avgInterval = 0;

// Iterate through the events
var event = null

while (iter.hasNext()) {
	event = iter.next()
	
	eventName = event.getName()
	if (eventName == "block_rq_insert") {
	
		// Save the state info
		tid = getEventFieldValue(event, "TID");
		sector = getEventFieldValue(event, "sector");
		if(tid == null) continue;
		
		//increase counters
		currReads++;
		countInsert ++;
		timestampInsert = event.getTimestamp();
		sector = parseInt(sector, 10)
		interval.push(sector, timestampInsert);
		
		cpu = getEventFieldValue(event, "context.cpu_id")
		cpu = cpu + " Block_Wait_Time";
		quark = ss.getQuarkAbsoluteAndAdd(cpu)
		cpuName = cpu + " " + sector
		ss.modifyAttribute(event.getTimestamp().toNanos(), cpuName, quark);
		
	} else if (eventName == "block_rq_issue") {
		tid = getEventFieldValue(event, "TID");
		if(tid == null) continue;
		
		sector = getEventFieldValue(event, "sector");
		currReads = currReads - 1;
		countIssue++;
		
		cpu = getEventFieldValue(event, "context.cpu_id")
		
		cpuQueue = cpu + " Block_Wait_Time";
		cpuService = cpu + " Disk_Wait_Time";
		
		quark = ss.getQuarkAbsoluteAndAdd(cpuQueue)
		ss.removeAttribute(event.getTimestamp().toNanos(), quark);
		quark = ss.getQuarkAbsoluteAndAdd(cpuService);
		cpuService = cpu + " Disk_Wait_Time " + sector;
		
		ss.modifyAttribute(event.getTimestamp().toNanos(), cpuService, quark);
		
		//get the associated timestamp from issue (or start) to get time between insert and issue
		timestampIssue = event.getTimestamp()

		index = interval.indexOf(parseInt(sector, 10))

		if(index == -1) continue;
		spliced = interval.splice(index, 2);
		timestampstart = spliced.pop();
		timestampInterval = timestampIssue.getDelta(timestampstart);
		avgInterval += timestampInterval.toNanos()
		countAVG ++;
		
	} else if (eventName == "block_rq_complete") {
		tid = getEventFieldValue(event, "TID");
		if(tid == null) continue;
		countComplete++;
		
		cpu = getEventFieldValue(event, "context.cpu_id")
		sector = getEventFieldValue(event, "sector")
		cpuService = cpu + " Disk_Wait_Time";
		quark = ss.getQuarkAbsoluteAndAdd(cpuService);
		cpuService = cpuService + " " + sector
		ss.removeAttribute(event.getTimestamp().toNanos(), quark);
	}
}


if (event != null) {
	ss.closeHistory(event.getTimestamp().toNanos());
}
print("Amount of block_rq_insert events: " + countInsert);
print("Amount of block_rq_issue events: " + countIssue);
print("Amount of block_rq_complete events: " + countComplete);
print("Amount of assosicated insert and issue events: " + countAVG);
print("Total: " + avgInterval)
print("Average amount of latency: " + avgInterval/countAVG + " nanoseconds");

//Create a map and fill it
var map = new java.util.HashMap();
map.put(ENTRY_PATH, '*');
provider = createTimeGraphProvider(analysis, map);

if (provider != null) {
	// Open a time graph view displaying this provider
	openTimeGraphView(provider);
}

 
