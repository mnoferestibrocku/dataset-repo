from tqdm import tqdm
import os
from dataformatting import extract_data, perform_test, perform_thread_test
import re

datasets = ['trace_data_apache'] # dataset foldername, assumes folder's location is in trace_data, and that folder contains data.csv
dur_windows = [1, 5]   # consider windows using these duration partitions (seconds)
e_windows = [500, 1000]     # consider windows using these event paritions (number of events)

system_level = False
process_level = False
requirements = ["apache", "sql", "http"] # "" if no requirement (necessary for process level to not be equivalent to system_level)
thread_level = True
min_events = 150 # minimum number of events for a thread to be considered 
min_windows = 10 # minimum number of windows for a thread to be considered

non_overlapping = True
sliding_window = True

single_stage = True
two_stage = True

event_limit = -1  # -1 for no limit
dataset_limit = 10000


if not os.path.exists("data"):
    os.makedirs("data")


for dataset in datasets:
    print("Loading Data")
    datapath = "data/" + dataset
    events, timestamps, durations, entries= extract_data("trace_data/"+dataset+"/data.csv", event_limit)
    
    #### SYSTEM LEVEL ####
    if system_level:
        print("SYSTEM LEVEL")
        print("Duration windows")
        for dur in dur_windows:
            outpath = datapath+ "/system_dur_%d/"%dur
            # nonoverlapping, single stage
            print("nonoverlapping, single stage")
            perform_test(outpath, dur, events, timestamps, durations,
                         True, True, True, dataset_limit)
            # nonoverlapping, two stage
            print("nonoverlapping, two stage")
            perform_test(outpath, dur, events, timestamps, durations,
                         True, True, False, dataset_limit)
            # overlapping, single stage
            print("\noverlapping, single stage")
            perform_test(outpath, dur, events, timestamps, durations,
                         True, False, True, dataset_limit)
            # overlapping, two stage
            print("\noverlapping, two stage")
            perform_test(outpath, dur, events, timestamps, durations,
                         True, False, False, dataset_limit)
        print("Event windows")
        for e in e_windows:
            outpath = datapath+ "/system_events_%d/"%e
            # nonoverlapping, single stage
            print("nonoverlapping, single stage")
            perform_test(outpath, e, events, timestamps, durations,
                         False, True, True, dataset_limit)
            # nonoverlapping, two stage
            print("nonoverlapping, two stage")
            perform_test(outpath, e, events, timestamps, durations,
                         False, True, False, dataset_limit)
            # overlapping, single stage
            print("\noverlapping, single stage")
            perform_test(outpath, e, events, timestamps, durations,
                         False, False, True, dataset_limit)
            # overlapping, two stage
            print("\noverlapping, two stage")
            perform_test(outpath, e, events, timestamps, durations,
                         False, False, False, dataset_limit)
    
    if process_level or thread_level:
        print("Filtering data")
        p_events = []
        p_timestamps = []
        p_durations = []
        p_entries = []
        for x in tqdm(range(len(entries))):
            include = False
            for r in requirements:
                if r in entries[x]:
                    include = True
            if include:
                p_events.append(events[x])
                p_timestamps.append(timestamps[x])
                p_durations.append(durations[x])
                p_entries.append(entries[x])
        print("\nFiltering reduced %d items to %d"%(len(entries), len(p_entries)))

    if process_level and len(p_events) > 1:
        print("PROCESS LEVEL")
        
        print("Duration windows")
        for dur in dur_windows:
            outpath = datapath +"/process_dur_%d/"%dur
            # nonoverlapping, single stage
            print("nonoverlapping, single stage")
            perform_test(outpath, dur, p_events, p_timestamps, p_durations,
                         True, True, True, dataset_limit)
            # nonoverlapping, two stage
            print("nonoverlapping, two stage")
            perform_test(outpath, dur, p_events, p_timestamps, p_durations,
                         True, True, False, dataset_limit)
            # overlapping, single stage
            print("\noverlapping, single stage")
            perform_test(outpath, dur, p_events, p_timestamps, p_durations,
                         True, False, True, dataset_limit)
            # overlapping, two stage
            print("\noverlapping, two stage")
            perform_test(outpath, dur, p_events, p_timestamps, p_durations,
                         True, False, False, dataset_limit)
        print("Event windows")
        for e in e_windows:
            outpath = datapath+ "/process_events_%d/"%e
            # nonoverlapping, single stage
            print("nonoverlapping, single stage")
            perform_test(outpath, e, p_events, p_timestamps, p_durations,
                         False, True, True, dataset_limit)
            # nonoverlapping, two stage
            print("nonoverlapping, two stage")
            perform_test(outpath, e, p_events, p_timestamps, p_durations,
                         False, True, False, dataset_limit)
            # overlapping, single stage
            print("\noverlapping, single stage")
            perform_test(outpath, e, p_events, p_timestamps, p_durations,
                         False, False, True, dataset_limit)
            # overlapping, two stage
            print("\noverlapping, two stage")
            perform_test(outpath, e, p_events, p_timestamps, p_durations,
                         False, False, False, dataset_limit)
    elif process_level and len(p_events) <= 1:
        print("Not enough process level data")

    t_events = []
    t_timestamps = []
    t_durations = []
    if thread_level:
        print("THREAD LEVEL")
        tid_id = [re.search("tid=\d+", x).group() for x in p_entries]
        tids = sorted(list(set(tid_id)))
        print("Number of threads: ", len(tids))
        
        for tid in tqdm(tids):
            indices = [i for i, x in enumerate(tid_id) if x == tid]
            if len(indices) > min_events:
                temp_events = []
                temp_timestamps = []
                temp_durations = []
                for x in indices:
                    temp_events.append(p_events[x])
                    temp_timestamps.append(p_timestamps[x])
                    temp_durations.append(p_durations[x])
                t_events.append(temp_events)
                t_timestamps.append(temp_timestamps)
                t_durations.append(temp_durations)

    
    if thread_level and len(t_events) > 1:
        print("Duration windows")
        for dur in dur_windows:
            outpath = datapath +"/thread_dur_%d/"%dur
            # nonoverlapping, single stage
            print("nonoverlapping, single stage")
            perform_thread_test(outpath, dur, t_events, t_timestamps, t_durations,
                         True, True, True, dataset_limit)
            # nonoverlapping, two stage
            print("nonoverlapping, two stage")
            perform_thread_test(outpath, dur, t_events, t_timestamps, t_durations,
                         True, True, False, dataset_limit)
            # overlapping, single stage
            print("\noverlapping, single stage")
            perform_thread_test(outpath, dur, t_events, t_timestamps, t_durations,
                         True, False, True, dataset_limit)
            # overlapping, two stage
            print("\noverlapping, two stage")
            perform_thread_test(outpath, dur, t_events, t_timestamps, t_durations,
                         True, False, False, dataset_limit)
        print("Event windows")
        for e in e_windows:
            outpath = datapath+ "/thread_events_%d/"%e
            # nonoverlapping, single stage
            print("nonoverlapping, single stage")
            perform_thread_test(outpath, e, t_events, t_timestamps, t_durations,
                         False, True, True, dataset_limit)
            # nonoverlapping, two stage
            print("nonoverlapping, two stage")
            perform_thread_test(outpath, e, t_events, t_timestamps, t_durations,
                         False, True, False, dataset_limit)
            # overlapping, single stage
            print("\noverlapping, single stage")
            perform_thread_test(outpath, e, t_events, t_timestamps, t_durations,
                         False, False, True, dataset_limit)
            # overlapping, two stage
            print("\noverlapping, two stage")
            perform_thread_test(outpath, e, t_events, t_timestamps, t_durations,
                         False, False, False, dataset_limit)
            
    elif thread_level and len(t_events) <= 1:
        print("Not enough thread level data")
