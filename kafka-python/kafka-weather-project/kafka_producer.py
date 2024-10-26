from kafka import KafkaProducer
import json
import time
import pandas as pd

# Load the weather dataset
df = pd.read_csv('Cleaned_GlobalWeather.csv')

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Update if your broker runs on a different host/port
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializing data to JSON format
)

# Sending data every second for a limited time (60 seconds)
try:
    start_time = time.time()  # Record the start time
    for index, row in df.iterrows():
        # Prepare data point to be sent
        data_point = {
            'location': row['location_name'],
            'temperature': row['temperature_celsius'],
            'humidity': row['humidity'],
            'precipitation': row['precip_mm']
        }

        # Send the data point to the Kafka topic
        producer.send('global_weather', value=data_point)
        print(f"Sent: {data_point}")

        # Check if 60 seconds have passed
        if time.time() - start_time >= 60:
            break  # Exit the loop after 60 seconds

        time.sleep(1)  # Wait for 1 second before sending the next data point

finally:
    producer.close()  # Close the producer when done
    print("Producer stopped after 60 seconds.")
