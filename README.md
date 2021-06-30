# kafka-p1
Test Kafka Project using Python, Docker &amp; MS SQL Server on Linux

Environment Setup:
OS: Ubuntu 20.04 LTS

1. Install Docker & Docker Compose
2. Install Azure Data Studio & VS Code
3. Open Terminal and start the containers
```
# start a a ms-sql-Server 2017 database in docker
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Password1#' --name mssqldb-2017 -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest

# start a 4 node confluent kafka cluster in docker 
docker-compose up -d
```
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
7. Execure the Python Producer and Consumer files inside the python virtual environment.
