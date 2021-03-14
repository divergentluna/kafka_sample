from datetime import datetime
import struct

from kafka import KafkaConsumer

topic_name = 'input'
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer('input',
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='latest')
for msg in consumer:
    time_value = msg.value.decode('utf-8')
    rfc_3339_format = datetime.utcfromtimestamp(float(time_value)/1000)
    print(f"timestamp:{rfc_3339_format}")


