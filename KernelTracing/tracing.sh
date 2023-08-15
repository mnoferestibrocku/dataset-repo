#!/bin/bash

echo "Test started"
start_time=$(date +%s)
echo "Enter the destination folder: "
read output_folder

lttng create my-session --output=$output_folder

lttng enable-channel --kernel --subbuf-size=64M --num-subbuf=8 my-kernel-channel
lttng enable-event --kernel --channel=my-kernel-channel --syscall --all
lttng add-context --kernel --channel=my-kernel-channel --type=procname
lttng add-context --kernel --channel=my-kernel-channel --type=pid
lttng add-context --kernel --channel=my-kernel-channel --type=tid
read -p "Press enter to start tracing for $duration s"

time=$(date +%s)
echo "${time} : START TRACING!!!"
lttng start

sleep 1200

time=$(date +%s)
echo "${time} : START CPU NOISE!!!"
stress-ng --matrix 6 --matrix-method prod --matrix-size 256 --timeout 120

sleep 60

time=$(date +%s)
echo "${time} : START IO NOISE!!!"
stress-ng --iomix 6 --timeout 120

sleep 60

time=$(date +%s)
echo "${time} : START SOCKET NOISE!!!"
stress-ng --sock 6 --timeout 120

sleep 60

time=$(date +%s)
echo "${time} : START MEMORY NOISE!!!"
stress-ng --vm 6 --vm-bytes 4G --timeout 120

sleep 60

lttng stop
lttng destroy my-session
time=$(date +%s)
echo "${time} : FINISH!!!"
