from flask import Flask, render_template, request
import time
from database       import Database

app         = Flask(__name__)

database    = Database()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/api/get")
def get():
    return database.put_water(34.4)

@app.route("/api/put/<channel>")
def put(channel):
    if not isinstance(channel, str):
        return "False"
    data = None
    try:
        data = float(request.args.get('value'))
    except Exception:
        return "False"
    print(data)
    match channel:
        case "water":
            return str(database.put_water(data))
        case "air":
            return str(database.put_air(data))
        case "humid":
            return str(database.put_humid(data))
        case "voltage":
            return str(database.put_voltage(data))
        case "soc":
            return str(database.put_soc(data))
        case _:
            pass
    return "False"

@app.route("/api/put")
def put_all():
    success = False
    t = time.time()

    try:
        data = float(request.args.get('water'))
        if data is not None:
            database.put_water(data, t)
        success = True
    except Exception:
        pass

    try:
        data = float(request.args.get('air'))
        if data is not None:
            database.put_air(data, t)
        success = True
    except Exception:
        pass

    try:
        data = float(request.args.get('humid'))
        if data is not None:
            database.put_humid(data, t)
        success = True
    except Exception:
        pass

    try:
        data = float(request.args.get('voltage'))
        if data is not None:
            database.put_voltage(data, t)
        success = True
    except Exception:
        pass

    try:
        data = float(request.args.get('soc'))
        if data is not None:
            database.put_soc(data, t)
        success = True
    except Exception:
        pass

    return str(success)

    

@app.route("/api/fetch/<time>")
def fetch(time):
    try:
        water   = database.get_water(float(time))
        air     = database.get_air(float(time))
        humid   = database.get_humid(float(time))
        voltage = database.get_voltage(float(time))
        soc     = database.get_soc(float(time))
        return {'water': water, 'air': air, 'humid': humid, 'voltage': voltage, 'soc': soc}
    except Exception:
        return ["Error"]
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)