from kafka import KafkaConsumer

topic_name = 'output'
bootstrap_servers = 'localhost:9092'
consumer = KafkaConsumer('input',
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='earliest')
for msg in consumer:
    print(f"timestamp:{msg.value.isoformat()}")
