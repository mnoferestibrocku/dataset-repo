# After installing "Linux Ubuntu 22.04.2 LTS", containing default applications and devoid of any third-party software installations, you need to follow the following steps to install the necessary tools:

## Step 1 : INSTALL LTTNG
## The docs found at https://lttng.org/docs/v2.12/ a good job of explaining how to install LTTng. However we add the commands here:
## Add the LTTng Stable 2.12 PPA repository and update the list of packages:

sudo apt-add-repository ppa:lttng/stable-2.12
sudo apt-get update

## Install the main LTTng 2.12 packages:

sudo apt-get install lttng-tools
sudo apt-get install lttng-modules-dkms
sudo apt-get install liblttng-ust-dev
sudo apt-get install liblttng-ust-agent-java


## Step 2 : INSTALL JAVA 

sudo apt-get install openjdk-18-jdk


## Step 3 : INSTALL Elasticsearch and Kibana

wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
sudo apt-get update && sudo apt-get install elasticsearch
sudo apt-get install kibana
sudo apt-get install logstash

## Step 4 : Download and Import Dataset
## Sign to the site and Download the file from https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot
## After extract the dataset, move "Edge-IIoTset dataset/Selected dataset for ML and DL/DNN-EdgeIIoT-dataset.csv" into the home dirextory
## Go to address http://localhost:5601/ in your browser and login to kibana (default username='elastic' and password='elastic')
## Create new index in elasticsearch
## Download import.py and put it in the home directory
## Run import.py
python import.py

## Step 5 : INSTALL stress-ng
sudo apt-get install stress-ng

