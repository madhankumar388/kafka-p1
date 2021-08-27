# kafka-p1 [![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/madhankumar388/kafka-p1)

 - Test Kafka Project using Python, Docker &amp; MS SQL Server on Linux

Reference : https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html

- Environment Setup:
OS: Ubuntu 20.04 LTS (WSL or VirtualMachine - prefferd )

1. Install Docker & Docker Compose
2. Install Azure Data Studio & VS Code
3. Clone this repo and switch to main branch
4. Open Terminal and start the containers
  ```
docker compose up -d
  ```
5.  Open Confluent Contrl Center link below and wait till the cluster is healthy.\ 
http://localhost:9021/clusters

6. Create Python Virtual enviromnment, activate it and install requirements.txt\
   https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
```
python3 -m venv my-test-env
source my-test-env/bin/activate
python3 -m pip install -r requirements.txt
```
7. Install the Microsoft ODBC driver for SQL Server (Linux)\
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15

8. Start Jupyterlap lab and open it in your browser
```
jupyter lab --no-browser
# wsl --shutdown if you are unable to open jupyterlab on local host
```
9.1 Install JDBC Sink connector in the connect container, and copy the config files into the container
```
docker exec -it connect /bin/bash
confluent-hub install confluentinc/kafka-connect-jdbc:latest
option 2
N
/home/appuser/pluggins
y
y

docker cp /home/madhan/git/kafka-p1/connect-avro-standalone.properties connect:/etc/schema-registry/connect-avro-standalone.properties
docker cp /home/madhan/git/kafka-p1/connector.properties connect:/etc/schema-registry/connector.properties
```
9.2 Start the connector
```
/bin/connect-standalone /etc/schema-registry/connect-avro-standalone.properties /etc/schema-registry/connector.properties
```
9.3 Execute the Python Producer (source/my_producer1.ipynb) inside the python virtual environment.
9.4 Login to the database using Data Studio and see the magic happen.


10.1 Execute the Python Producer (source/my_producer2.ipynb) inside the python virtual environment.
10.2 Create a File Sink connector using Confluent control center to stream the records to an output file, refer info.txt.
