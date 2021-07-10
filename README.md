# kafka-p1 [![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/madhankumar388/kafka-p1)

 - Test Kafka Project using Python, Docker &amp; MS SQL Server on Linux

Reference : https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html

Environment Setup:
OS: Ubuntu 20.04 LTS (WSL or VirtualMachine - prefferd )

1. Install Docker & Docker Compose
2. Install Azure Data Studio & VS Code
3. Open Terminal and start the containers
```
# start a a ms-sql-Server 2017 database in docker
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Password1#' --name mssqldb-2017 -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest

# start a 4 node confluent kafka cluster in docker 
docker-compose up -d
```
Note:  Check if Confluent Contrl center is up and cluster is healthy before proceeding , wait for few mins for cluster to be healthy . 
http://localhost:9021/clusters

4. Restore the Database backup file to MSSQL ServerDB using Azure Data Studio UI
5. Create Python Virtual enviromnment, activate it and install requirements.txt\
   https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
```
python3 -m venv my-test-env
source my-test-env/bin/activate
python3 -m pip install -r requirements.txt
```
6. Install the Microsoft ODBC driver for SQL Server (Linux)\
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15
7. Execute the Python Producer (mssql-pyodbc.py) inside the python virtual environment.
8. Avro Schema for the Key and value of the records can be found in the repo info.txt
9. Create a File Sink connector using Confluent control center to stream the records to an output file.

