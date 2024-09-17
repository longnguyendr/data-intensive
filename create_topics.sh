#!/bin/bash

# Wait for Kafka to be ready
echo "Waiting for Kafka to start..."
while ! nc -z localhost 9092; do
  sleep 1
done

# Check if the topic 'log_data' already exists
EXISTING_TOPIC=$(kafka-topics.sh --list --bootstrap-server localhost:9092 | grep -w log_data)

if [ -z "$EXISTING_TOPIC" ]; then
  # If the topic does not exist, create it
  echo "Creating topic 'log_data'"
  kafka-topics.sh --create --topic log_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
else
  echo "Topic 'log_data' already exists, skipping creation."
fi

# Add any additional topics if needed
# kafka-topics.sh --create --topic another_topic --bootstrap-server localhost:9092 --partitions 2 --replication-factor 1
