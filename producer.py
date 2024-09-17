from kafka import KafkaProducer
import json
import time
import random

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Adjust this if running outside Docker
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

log_levels = ["INFO", "ERROR", "DEBUG", "WARN"]

# Function to generate log data
def generate_log():
    log = {
        'timestamp': time.time(),
        'level': random.choice(log_levels),
        'message': f"Log message {random.randint(1, 100)}"
    }
    return log

# Sending log data to Kafka topic 'log_data'
while True:
    log_data = generate_log()
    print(f"Sending: {log_data}")
    producer.send('log_data', value=log_data)
    time.sleep(2)  # Adjust the interval as needed
