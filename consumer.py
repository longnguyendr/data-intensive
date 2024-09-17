from kafka import KafkaConsumer
import psycopg2
import json

# Kafka Consumer configuration
consumer = KafkaConsumer(
    'log_data',
    bootstrap_servers='localhost:9092',  # Adjust this if running outside Docker
    auto_offset_reset='earliest',  # Start reading from the earliest available message
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="mydb",
    user="user",
    password="password",
    host="localhost",  # Change this if running outside Docker
    port=65432  # Ensure the correct port (based on your Docker setup)
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id SERIAL PRIMARY KEY,
        timestamp BIGINT,
        level VARCHAR(10),
        message TEXT
    );
""")
conn.commit()

# Processing Kafka messages
for message in consumer:
    log_data = message.value
    # Only store logs that are not DEBUG
    if log_data['level'] != "DEBUG":
        print(f"Storing log: {log_data}")
        cur.execute("INSERT INTO logs (timestamp, level, message) VALUES (%s, %s, %s)",
                    (log_data['timestamp'], log_data['level'], log_data['message']))
        conn.commit()
