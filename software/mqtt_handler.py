import threading
import paho.mqtt.client as mqtt

class MQTTHandler:
    def __init__(self, ip: str = "mosquitto", port: int = 1883, topic: str = "test/topic"):
        self.ip = ip
        self.port = port
        self.topic = topic

        # Initialize MQTT client
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Connect to the broker
        self.client.connect(self.ip, self.port, 60)

        # Start loop in separate thread
        self.thread = threading.Thread(target=self.client.loop_forever)
        self.thread.daemon = True  # Allow thread to exit when main thread exits
        self.thread.start()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to {self.ip}:{self.port} with result code {rc}")
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(f"[{msg.topic}] {msg.payload.decode()}")

    def publish(self):
        return self.client.publish(self.topic, "hej")