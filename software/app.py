from flask import Flask
import time

from database import Database

app = Flask(__name__)

database = Database("")
database.put_water(1.0, 10.0)
database.put_water(2.0, 11.0)
database.put_water(3.0, 12.0)
database.put_water(4.0, 13.0)


@app.route("/")
def hello():
    return database.put_water(34.5, 34.4)

@app.route("/api/get")
def get():
    return database.put_water(34.5, 34.4)

@app.route("/api/put")
def put():
    return database.put_water(34.5, 34.4)

@app.route("/api/fetch/<time>")
def fetch(time):
    try:
        water   = database.get_water(float(time))
        air     = database.get_air(float(time))
        humid   = database.get_humid(float(time))
        return {'water': water, 'air': air, 'humid': humid}
    except Exception:
        return ["Error"]
    