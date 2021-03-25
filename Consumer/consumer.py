from datetime import datetime

from kafka import KafkaConsumer
from kafka import KafkaProducer

consumer_topic_name = 'input'
bootstrap_servers = '0.0.0.0:9092'
consumer = KafkaConsumer(consumer_topic_name,
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='latest')

producer_topic_name = 'output'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

for msg in consumer:
    time_value = msg.value.decode('utf-8')
    rfc_3339_format = str(datetime.utcfromtimestamp(float(time_value)/1000))
    print(f"timestamp:{rfc_3339_format}")

    producer.bootstrap_connected()
    rfc_3339_encoded = rfc_3339_format.encode('utf-8')
    producer.send(producer_topic_name, rfc_3339_encoded)
    print('msg sent!')

