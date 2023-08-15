# After installing "Linux Ubuntu 22.04.2 LTS", containing default applications and devoid of any third-party software installations, you need to follow the following steps to install the necessary tools:

## Step 1 : INSTALL LTTNG
## The docs found at https://lttng.org/docs/v2.12/ a good job of explaining how to install LTTng. However we add the commands here:
## Add the LTTng Stable 2.12 PPA repository and update the list of packages:

apt-add-repository ppa:lttng/stable-2.12
apt-get update

## Install the main LTTng 2.12 packages:

apt-get install lttng-tools
apt-get install lttng-modules-dkms
apt-get install liblttng-ust-dev
apt-get install liblttng-ust-agent-java


## Step 2 : INSTALL JAVA 



## Step 3 : INSTALL stress-ng

apt-get install stress-ng
