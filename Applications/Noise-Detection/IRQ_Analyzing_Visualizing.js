// Load the proper modules
loadModule("/TraceCompass/Trace")
loadModule("/TraceCompass/Analysis")
loadModule("/TraceCompass/DataProvider")
loadModule("/TraceCompass/View")

// Get the active trace
var trace = getActiveTrace()

// Get an event iterator on that trace
var iter = getEventIterator(trace)

// Load Linux Kernel analysis
var LKanalysis = getTraceAnalysis(trace, "Linux Kernel");
if (LKanalysis == null) {
	print("Linux Kernel analysis not available");
} else {
	// Schedule the analysis
	LKanalysis.schedule();
	// Wait for the LKanalysis to complete
    LKanalysis.waitForCompletion();
}

// Get the analysis's state system so we can fill it
var LKSS = LKanalysis.getStateSystem();
if(LKSS == null){
	print("Error with LKSS");
}else{
	print(LKanalysis.waitForInitialization());
	print(LKanalysis);
	}


//Create an analysis
var analysis = createScriptedAnalysis(trace, 'IRQ Noise Analysis');

// Get the analysis's state system so we can fill it
var ss = analysis.getStateSystem(false);

//hold information about cpu interrupted
longestInterrupt=0;
totalInterrupt=0;
interruptCount=0;

// Iterate through the events
var event = null

while (iter.hasNext()) {
	event = iter.next()
	
	eventName = event.getName()
	if (eventName == "irq_handler_entry") {
		tid = getEventFieldValue(event, "TID");
		
		//if tid == null no process was interrupted -> skip event
		if(tid == null | tid == 0){
		continue;
		}
	
		//Tid is value, save state info
		irqDisplayOnGraph = "IRQ: ";
		irq = getEventFieldValue(event, "irq");
		irqDisplayOnGraph += irq;
		name = getEventFieldValue(event, "name");
		cpu = getEventFieldValue(event, "CPU");	
		
		quark = ss.getQuarkAbsoluteAndAdd(irqDisplayOnGraph);
		ss.modifyAttribute(event.getTimestamp().toNanos(), irqDisplayOnGraph, quark);		
					
		//get quark of current thread that was interrupted by irq
		quark = LKSS.getQuarkAbsolute('CPUs', cpu, 'Current_thread');
		currInterval = (LKSS.querySingleState(event.getTimestamp().toNanos(),quark));
		
		//set name for new graphs
		name = "TID: " + tid + " CPU: " + cpu + " IRQ: " + irq; 
		
		//of the thread interrupted draw entire thread
		quark = ss.getQuarkAbsoluteAndAdd(name)
		ss.modifyAttribute(currInterval.getStartTime(), name, quark);
		ss.removeAttribute(currInterval.getEndTime(), quark);
		
	} else if (eventName == "irq_handler_exit") {
		//Remove the waiting for exit
		irq = "IRQ: ";
		irq += getEventFieldValue(event, "irq")
		quark = ss.getQuarkAbsoluteAndAdd(irq);
		ss.removeAttribute(event.getTimestamp().toNanos(), quark);
	} 
}


if (event != null) {
	ss.closeHistory(event.getTimestamp().toNanos());
}

//Create a map and fill it
var map = new java.util.HashMap();
map.put(ENTRY_PATH, '*');
provider = createTimeGraphProvider(analysis, map);

if (provider != null) {
	// Open a time graph view displaying this provider
	openTimeGraphView(provider);
}
filter = org.eclipse.tracecompass.tmf.core.signal.TmfSignalManager.dispatchSignal(new org.eclipse.tracecompass.analysis.os.linux.core.signals.TmfThreadSelectedSignal(this, tid, trace));
showView("org.eclipse.linuxtools.tmf.analysis.graph.ui.criticalpath.view.criticalpathview");
//print('filter')
applyGlobalFilter(filter);


