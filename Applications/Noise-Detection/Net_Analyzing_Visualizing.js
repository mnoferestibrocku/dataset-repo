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
var analysis = createScriptedAnalysis(trace, 'Network Noise');

// Get the analysis's state system so we can fill it
var ss = analysis.getStateSystem(false);

//counter and current reads initalization.
netDevCounter = 0;
netSKBCounter = 0;
totalDev = 0;
totalSKB = 0;
intervalQueue = [];	
intervalSKB = [];

// Iterate through the events
var event = null

while (iter.hasNext()) {
	event = iter.next()
	
	eventName = event.getName()
	
	if (eventName == "net_dev_queue") {
	tid = getEventFieldValue(event, "TID");
	if(tid == null | tid == 0) continue;
	netDevCounter++;
	intervalQueue.push(parseInt(tid, 10), event)
	
	quark = ss.getQuarkAbsoluteAndAdd('Trs_Wait_Time')
	ss.modifyAttribute(event.getTimestamp().toNanos(), tid, quark);
	
	
	}else if (eventName == "irq_softirq_entry") {
	tid = getEventFieldValue(event, "TID");
	if(tid == null | tid == 0) continue;
	index = intervalQueue.indexOf(parseInt(tid, 10))
	if(index == -1) continue;
	spliced = intervalQueue.splice(index, 2);
	startEvent = spliced.pop();
	
	//show on ss
	quark = ss.getQuarkAbsoluteAndAdd('Trs_Wait_Time')
	ss.removeAttribute(event.getTimestamp().toNanos(), quark);
	
	//get a total, max, and average
	timeIntervalStart = startEvent.getTimestamp();
	timeIntervalEnd = event.getTimestamp();
	timestampInterval = timeIntervalEnd.getDelta(timeIntervalStart);
	totalDev += timestampInterval.toNanos();
	
	
	
	
	
	} else if (eventName == "net_if_receive_skb"){
	tid = getEventFieldValue(event, "TID");
	if(tid == null | tid == 0) continue;
	netSKBCounter++;
	intervalSKB.push(parseInt(tid, 10), event)
	
	quark = ss.getQuarkAbsoluteAndAdd('Rcv_Wait_Time')
	ss.modifyAttribute(event.getTimestamp().toNanos(), tid, quark);
		
		
	} else if (eventName == "sched_waking"){
	tid = getEventFieldValue(event, "TID");
	if(tid == null | tid == 0) continue;
	index = intervalSKB.indexOf(parseInt(tid, 10))
	if(index == -1) continue;
	spliced = intervalSKB.splice(index, 2);
	startEvent = spliced.pop();
	
	//show on ss
	quark = ss.getQuarkAbsoluteAndAdd('Rcv_Wait_Time')
	ss.removeAttribute(event.getTimestamp().toNanos(), quark);
	
	//get a total, max, and average
	timeIntervalStart = startEvent.getTimestamp();
	timeIntervalEnd = event.getTimestamp();
	timestampInterval = timeIntervalEnd.getDelta(timeIntervalStart);
	totalSKB += timestampInterval.toNanos();
	}
}


if (event != null) {
	ss.closeHistory(event.getTimestamp().toNanos());
}
print("Net Dev: " + netDevCounter);
print(totalDev);
print(" ")
print("SKB: " + netSKBCounter);
print(totalSKB);
print(" ")

//Create a map and fill it
var map = new java.util.HashMap();
map.put(ENTRY_PATH, '*');
provider = createTimeGraphProvider(analysis, map);

if (provider != null) {
	//Open a time graph view displaying this provider
	openTimeGraphView(provider);
}//

 
