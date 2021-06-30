from kafka import KafkaProducer
from kafka.vendor.six import b
producer = KafkaProducer(bootstrap_servers='localhost:9091')
for i in range(10):
    Message = 'Message: ' + str(i)
    producer.send('foobar', key=b'test-key', value=b(Message))
producer.flush()