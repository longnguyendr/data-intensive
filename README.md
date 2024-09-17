Testing message broker

## Prerequisites:

- Python 3.10 or higher
- kafka-python library
- Docker engine
- Docker-compose

## How to run:

1. Start the Kafka broker:

```
docker-compose up -d --build
```

2. create virtual environment and install the requirements:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the producer:

```
python producer.py
```

4. Run the consumer:

```
python consumer.py
```
