from paho.mqtt import client


class MQTTHandler:
    def __init__(self, ip: str, port: int):
        self.client = client.Client()
        self.client.connect(ip, port, 60)