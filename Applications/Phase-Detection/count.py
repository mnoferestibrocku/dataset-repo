data = open("trace_data/trace_data_elk2/data.csv")
d = data.readline()
count = 0
while d: 
    if "syscall" in d:
        count += 1
    if count != 0 and int(count/10000) == count/10000:
        print(count)
    d = data.readline()

print("Total number of syscall events:", count)
data.close()