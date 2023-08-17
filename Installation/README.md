To establish the necessary environment after installing "Linux Ubuntu 22.04.2 LTS," which includes the default applications and excludes any third-party software installations, you can utilize the "[installation.sh](https://github.com/mnoferestibrocku/dataset-repo/tree/main/Installation/installation.sh)" script.
This script encompasses the subsequent steps:

- **Step 1:** Install LTTNG
  
The documentation available at https://lttng.org/docs/v2.12/ does an excellent job of explaining how to install LTTng. Nonetheless, we've included the necessary commands here for your convenience:

To begin, add the LTTng Stable 2.12 PPA repository and refresh the list of packages by executing the following commands:
```
sudo apt-add-repository ppa:lttng/stable-2.12
sudo apt-get update
```
To install the primary LTTng 2.12 packages, use the following command:
```
sudo apt-get install lttng-tools
sudo apt-get install lttng-modules-dkms
sudo apt-get install liblttng-ust-dev
sudo apt-get install liblttng-ust-agent-java
```

- **Step 2:** Install Java

```
sudo apt-get install openjdk-18-jdk
```

- **Step 3:** Install Elasticsearch and Kibana
  
```
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
sudo apt-get update && sudo apt-get install elasticsearch
sudo apt-get install kibana
sudo apt-get install logstash
```

- **Step 4:** Download and Import Dataset into Elasticsearch

Here's a step-by-step guide on how to perform the tasks you mentioned:

1. **Download the Dataset:**
   - Go to the website: [https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot](https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot)
   - Sign in to the site.
   - Download the file "DNN-EdgeIIoT-dataset.csv" from the dataset.

2. **Extract and Move the Dataset:**
   - Extract the downloaded dataset to a folder of your choice.
   - Locate the file "DNN-EdgeIIoT-dataset.csv" within the extracted folder.
   - Move the "DNN-EdgeIIoT-dataset.csv" file to your home directory.

3. **Access Kibana:**
   - Open your web browser.
   - In the address bar, enter: [http://localhost:5601/](http://localhost:5601/).
   - This should take you to the Kibana interface.

4. **Login to Kibana:**
   - You'll be prompted to log in. The default username and password are usually:
     - Username: `elastic`
     - Password: `elastic`
   - Enter these credentials to log in.

5. **Create a New Index in Elasticsearch:**
   - Once logged in to Kibana, follow these steps:
     - Click on "Management" in the left-hand navigation menu.
     - Under "Stack Management," click on "Index Patterns."
     - Click on the "Create index pattern" button.
     - In the "Index pattern" field, enter the name of your index pattern.(e.g., "dnniotdataset").
     - Click the "Next step" button.
     - In the "Time Filter field name" dropdown, select the appropriate time field for your dataset (if applicable).
     - Click the "Create index pattern" button.

That's it! You've successfully set up the dataset in Elasticsearch through Kibana. You can now proceed with your analysis using the tools and features provided by Elasticsearch and Kibana.
```

```
Download import.py and put it in the home directory
Run import.py
```
python import.py
```

- **Step 5:** Create Workloads

Download workloads from the Workloads directory
```
curl -XPUT "http://localhost:9200/_watcher/watch/lightloadid" -H "Content-Type: application/json" -d @lightload_watcher.json
curl -XPUT "http://localhost:9200/_watcher/watch/highloadid" -H "Content-Type: application/json" -d @highload_watcher.json
```

- **Step 6:** Install stress-ng

```
sudo apt-get install stress-ng
```
