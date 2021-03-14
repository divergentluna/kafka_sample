from time import time, sleep
import pickle

from kafka import KafkaProducer


topic_name = 'input'
bootstrap_servers = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# generate messages
while True:
    producer.bootstrap_connected()

    msg = str(time() * 1000)
    encoded_msg = msg.encode('utf-8')
    producer.send(topic_name, encoded_msg)

    print(f'Sending msg: {msg}')
    sleep(30)
