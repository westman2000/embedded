import board
import adafruit_si7021
import os
import time
import sys
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'localhost'
#ACCESS_TOKEN = 'DHT22_DEMO_TOKEN'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

sensor = adafruit_si7021.SI7021(board.I2C())

sensor_data = {'temperature': 0, 'humidity': 0}

next_reading = time.time()

client = mqtt.Client()

# Set access token
#client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:
        #print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(sensor.temperature, sensor.relative_humidity))
        sensor_data['temperature'] = sensor.temperature
        sensor_data['humidity'] = sensor.relative_humidity

        # Sending humidity and temperature data to ThingsBoard
        client.publish('mqtt/pimylifeup', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()

