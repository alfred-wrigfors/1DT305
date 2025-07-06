from flask import Flask

import time

from database       import Database
from mqtt_handler   import MQTTHandler

app         = Flask(__name__)
mqtt        = MQTTHandler()
mqtt2        = MQTTHandler()

database    = Database()

@app.route("/")
def hello():
    return database.put_water(34.4)

@app.route("/api/get")
def get():
    return database.put_water(34.4)

@app.route("/api/put")
def put():
    print(mqtt.publish())
    return str(database.put_water(34.4))

@app.route("/api/fetch/<time>")
def fetch(time):
    try:
        water   = database.get_water(float(time))
        air     = database.get_air(float(time))
        humid   = database.get_humid(float(time))
        return {'water': water, 'air': air, 'humid': humid}
    except Exception:
        return ["Error"]
    