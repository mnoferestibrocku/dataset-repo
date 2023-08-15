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
var analysis = createScriptedAnalysis(trace, 'Scheduler Noise');

// Get the analysis's state system so we can fill it
var ss = analysis.getStateSystem(false);



//change this value to the desired TID you want to trace
desiredTID = 22774;


//Array of events
iEvents = [];
totalInterval=0, eventCount=0, averageInterval=0, longestInterval=0, longestTimestamp=0;


// Iterate through the events
var event = null

while (iter.hasNext()) {
	event = iter.next()
	
	eventName = event.getName()
	
	if (eventName == "sched_switch") {
		//and tid is == to desired tid or next_tid
		tid = getEventFieldValue(event, "TID");
		nextTid = getEventFieldValue(event, "next_tid");
		if(tid == 0 | nextTid == 0){
		continue;
		}
		if(tid == desiredTID){
			iEvents.push(event);
			quark = ss.getQuarkAbsoluteAndAdd("Sched Noise")
			eventCount++
			name = "Event count: " + eventCount
			ss.modifyAttribute(event.getTimestamp().toNanos(), name, quark);
			
		} else if(desiredTID == nextTid){
			iEvents.push(event);
			quark = ss.getQuarkAbsoluteAndAdd("Sched Noise")
			ss.removeAttribute(event.getTimestamp().toNanos(), quark);
		} 
		
	
	//if the process we're following exits then we exit
	}else if (eventName == "sched_process_exit"){
		tid = getEventFieldValue(event, "TID");
		if(tid == desiredTID){
			break;
		}
	}
}


if (event != null) {
	ss.closeHistory(event.getTimestamp().toNanos());
}

//reverse the order of the array so that the newest is at the top
//then pop to get rid of the first sched_switch that gets onto the Desired TID
iEvents.reverse();
iEvents.pop();


eventsLength = iEvents.length/2;
for(i = 0; i < eventsLength; i ++){
eventStart = iEvents.pop();
intervalStart = eventStart.getTimestamp();
eventEnd = iEvents.pop();
intervalEnd = eventEnd.getTimestamp();
interval = intervalEnd.getDelta(intervalStart);

print(intervalStart + ", " + intervalEnd)

totalInterval += interval.toNanos();
}

print(eventCount + " number of events which took a total of " + totalInterval + " nanoseconds. On average the CPU was off process for " + (totalInterval/eventCount) + " nanoseconds");

//Create a map and fill it
var map = new java.util.HashMap();
map.put(ENTRY_PATH, '*');
provider = createTimeGraphProvider(analysis, map);

if (provider != null) {
	//Open a time graph view displaying this provider
	openTimeGraphView(provider);
}

 
