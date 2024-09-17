# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /workspace

# Copy requirements file to install dependencies
COPY requirements.txt /workspace/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Kafka port and PostgreSQL port for access
EXPOSE 9092 5432

# Command to keep the container running
CMD ["tail", "-f", "/dev/null"]
