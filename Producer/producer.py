from kafka import KafkaProducer
from time import time

topic_name = 'input'
bootstrap_servers = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# generate messages
# for _ in range(50):
while True:
    producer.bootstrap_connected()
    msg = str(time() * 1000)
    metrics = producer.metrics()
    producer.send(topic_name, msg.encode('utf-8'))
    print(f'Sending msg: {msg}')
