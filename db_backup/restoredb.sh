/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Password1# -Q"RESTORE DATABASE TestDB
FROM DISK = '/db_backup/TestDB-2021627-16-47-11.bak'
WITH REPLACE
GO"