from kafka import KafkaConsumer
import pandas as pd
import json  # Make sure to import json for deserialization
import time

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'global_weather',  # The name of the topic to subscribe to
    bootstrap_servers='localhost:9092',  # Update if your broker runs on a different host/port
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),  # Deserialize the JSON data
    auto_offset_reset='earliest',  # Start reading at the earliest message
    enable_auto_commit=True,  # Automatically commit offsets
    group_id='weather_group'  # Group ID for the consumer
)

# List to store consumed data
data_list = []

# Start time for consuming data
start_time = time.time()

# Consume messages for 60 seconds
print("Consuming messages...")

try:
    while True:
        # Check if 60 seconds have passed
        if time.time() - start_time >= 60:
            break  # Exit the loop after 60 seconds

        # Poll for new messages
        message = consumer.poll(timeout_ms=1000)  # Wait for messages

        for topic_partition, messages in message.items():
            for msg in messages:
                # Append the consumed message to the list
                data_list.append(msg.value)

finally:
    # Check if we received any data
    if data_list:
        # Create a DataFrame from the consumed data
        df = pd.DataFrame(data_list)

        # Save the DataFrame to a CSV file
        df.to_csv('consumed_weather_data.csv', index=False)
        print("Data saved to 'consumed_weather_data.csv'.")

        # Display summary statistics
        print("\nSummary Statistics:")
        print(df.describe())

        # Print the top 5 records
        print("\nTop 5 records:")
        print(df.head())
    else:
        print("No data consumed in the last 60 seconds.")

    # Close the consumer
    consumer.close()
