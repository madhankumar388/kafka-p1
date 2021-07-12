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
docker-compose up -d
  ```
5.  Open Confluent Contrl Center link below and wait till the cluster is healthy. 
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
8. Execute the Python Producer (mssql-pyodbc.py) inside the python virtual environment.
9. Avro Schema for the Key and value of the records can be found in the repo info.txt
10. Create a File Sink connector using Confluent control center to stream the records to an output file.

