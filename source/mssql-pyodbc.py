import pyodbc
import json
import datetime

from kafka import KafkaProducer
from kafka.vendor.six import b

producer = KafkaProducer(bootstrap_servers='localhost:9091', value_serializer=lambda v: json.dumps(v, cls=DateTimeEncoder).encode('utf-8') , key_serializer=str.encode)

#producer = KafkaProducer(bootstrap_servers='localhost:9091', )

server = 'localhost' 
database = 'TestDB' 
username = 'sa' 
password = 'Scooby1#' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

rows = cursor.execute('SELECT * FROM citadel ')

for row in rows :

    items = [dict(zip([key[0] for key in cursor.description], row))  for row in rows ]

    class DateTimeEncoder(json.JSONEncoder):
        def default(self, z):
            if isinstance(z, datetime.datetime):
                return (str(z))
            else:
                return super().default(z)


    for item in items:

#       print (json.dumps( item, cls=DateTimeEncoder))
        item_key=str(item["ext_acc"]) 
        producer.send('excesscash_topic',key=item_key, value=item)
        print (item_key, item)
producer.flush()