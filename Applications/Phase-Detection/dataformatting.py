import os
from get_windows import event_sliding_windows, duration_sliding_windows, duration_windows, event_windows, save_data, read_dataset
from cluster_windows import perform_clustering, perform_twostageclustering

def extract_data(filepath, limit=-1):
    d = open(filepath, 'r')
    header = d.readline().strip().split("\t")

    events = []
    timestamps = []
    durations = []
    entries = []

    count = 1

    # event, channel, timestamp
    queue = []
    item = d.readline().strip()
    while item:
        if "syscall" in item:
            y = item.split("\t")
            e = y[header.index("Event type")].replace("syscall_exit_", "").replace("syscall_entry_", "")
            temp = y[header.index("Timestamp")].replace(" ", "").split(":")
            t = (int(float(temp[2])*pow(10, 9)) + int(temp[1])*60*pow(10, 9) + int(temp[0])*pow(60, 2)*pow(10, 9))
            c = int(y[header.index("CPU")])

            if "entry" in y[header.index("Event type")]:
                queue.append([e, c, t])
            if "exit" in y[header.index("Event type")]:
                l = 0
                for x in range(len(queue)):
                    q = queue[x]
                    if c == q[1] and e == q[0]:
                        l = t - q[2]
                        queue.pop(x)
                        break
                durations.append(l)
                events.append(e)
                timestamps.append(t)
                entries.append(item)
            count += 1

        if count%1000000 == 0:
            print(count)
        if count == limit:
            break
        item = d.readline().strip()
    print()
    d.close()
    return events, timestamps, durations, entries

# is_duration_windows: true for dur paritioning, false for event paritioning
def perform_test(path, window_size, 
                 events, timestamps, durations,
                 is_duration_windows, is_overlapping, is_singlestage,
                 dataset_limit, step=1):
    filename = ""
    if is_overlapping:
        filename += "sliding"+str(int(step*100))
    else:
        filename += "nonoverlap"
    

    if os.path.exists(path+"data_"+filename+".csv") and os.path.exists(path+"data_"+filename+"_mod.csv"):
        dataset = read_dataset(path+"data_"+filename+".csv")
        mod_dataset = read_dataset(path+"data_"+filename+"_mod.csv")
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        if is_duration_windows:
            if is_overlapping:
                dataset, mod_dataset = duration_sliding_windows(events, timestamps, durations, window_size, step)
            else:
                dataset, mod_dataset = duration_windows(events, timestamps, durations, window_size)
        else:
            if is_overlapping:
                dataset, mod_dataset = event_sliding_windows(events, durations, window_size, step)
            else: 
                dataset, mod_dataset = event_windows(events, durations, window_size)
        if dataset_limit != -1 and len(dataset) > dataset_limit:
            dataset = dataset[:dataset_limit]
            mod_dataset = mod_dataset[:dataset_limit]
        save_data(dataset, path+filename+".csv")
        save_data(mod_dataset, path+filename+"_mod.csv")
    

    if is_singlestage:
        filename += "_onestage"
        perform_clustering(dataset, path+filename)
    else:
        filename += "_twostage"
        perform_twostageclustering(dataset, mod_dataset, path+filename)

def perform_thread_test(path, window_size, 
                 events, timestamps, durations,
                 is_duration_windows, is_overlapping, is_singlestage,
                 dataset_limit):
    filename = ""
    if is_overlapping:
        filename += "sliding"
    else:
        filename += "nonoverlap"
    

    if os.path.exists(path+"data_"+filename+".csv") and os.path.exists(path+"data_"+filename+"_mod.csv"):
        dataset = read_dataset(path+"data_"+filename+".csv")
        mod_dataset = read_dataset(path+"data_"+filename+"_mod.csv")
    else:
        if not os.path.exists(path):
            os.makedirs(path)
        dataset = []
        mod_dataset = []
        if is_duration_windows:
            if is_overlapping:
                for e in range(len(events)):
                    d, m = duration_sliding_windows(events[e], timestamps[e], durations[e], window_size)
                    dataset = dataset + d
                    mod_dataset = mod_dataset + m
            else:
                for e in range(len(events)):
                    d, m = duration_windows(events[e], timestamps[e], durations[e], window_size)
                    dataset = dataset + d
                    mod_dataset = mod_dataset + m
        else:
            if is_overlapping:
                for e in range(len(events)):
                    d, m = event_sliding_windows(events[e], durations[e], window_size)
                    dataset = dataset + d
                    mod_dataset = mod_dataset + m
            else: 
                for e in range(len(events)):
                    d, m = event_windows(events[e], durations[e], window_size)
                    dataset = dataset + d
                    mod_dataset = mod_dataset + m

        if dataset_limit != -1 and len(dataset) > dataset_limit:
            dataset = dataset[:dataset_limit]
            mod_dataset = mod_dataset[:dataset_limit]
        save_data(dataset, path+filename+".csv")
        save_data(mod_dataset, path+filename+"_mod.csv")
    

    if is_singlestage:
        filename += "_onestage"
        perform_clustering(dataset, path+filename)
    else:
        filename += "_twostage"
        perform_twostageclustering(dataset, mod_dataset, path+filename)