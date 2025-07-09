from flask import Flask, render_template, request
import time
from database       import Database
from collections import deque

app         = Flask(__name__)

database    = Database()

def split_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

@app.route("/")
def hello():
    return render_template('index.html')


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

    keyword_map = {
        "water"     : database.put_water,
        "air"       : database.put_air,
        "humid"     : database.put_humid,
        "voltage"   : database.put_voltage,
        "soc"       : database.put_soc,
    }

    for keyword in keyword_map.keys():
        try:
            data = float(request.args.get(keyword, t))
            if data is not None:
                keyword_map[keyword](data)
            success = True
        except Exception:
            pass

    return str(success)

def handle_data(list_param: list, n: int) -> list[dict]:
    data   = [item for item in list_param if item['value'] < 100]
    data   = sorted(data, key=lambda x: x['time'])
    data   = [{'time': sum([k['time'] for k in x]) / len(x), 'value': sum([k['value'] for k in x]) / len(x)} for x in split_list(data, n)]
    return data

@app.route("/api/fetch/<t>")
def fetch(t):
    n = 500
    try:
        t = time.time() - float(t)

        water   = handle_data(database.get_water(t), n)
        air     = handle_data(database.get_air(t), n)
        humid   = handle_data(database.get_humid(t), n)
        voltage = handle_data(database.get_voltage(t), n)
        soc     = handle_data(database.get_soc(t), n)

        return {'water': water, 'air': air, 'humid': humid, 'voltage': voltage, 'soc': soc}
    except Exception as e:
        return str(e)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)