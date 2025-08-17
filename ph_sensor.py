import paho.mqtt.client as mqtt
import random, time

client = mqtt.Client()
client.connect("127.0.0.1", 1883)

while True:
	ph = round(random.uniform(6.5, 8.0), 2)
	client.publish("sensor/ph", ph)
	if ph > 10.0: #ph=12.5 for Flag
		client.publish("system/status", "ALARM TRIGGERED")
	time.sleep(1)
