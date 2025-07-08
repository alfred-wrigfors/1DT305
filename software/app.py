from flask import Flask, render_template, request
import time
from database       import Database
from collections import deque

app         = Flask(__name__)

database    = Database()

def split_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]


# def moving_average(data, key, window_size, new_key = "value2"):
#     if not data or window_size <= 0:
#         return data  # handle empty input or invalid window

#     window = deque()
#     window_sum = 0.0

#     for i, item in enumerate(data):
#         value = item.get(key, 0)
#         window.append(value)
#         window_sum += value

#         # Ensure the window is of the correct size
#         if len(window) > window_size:
#             window_sum -= window.popleft()

#         avg = window_sum / len(window)
#         item[new_key] = avg

#     return data

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



@app.route("/api/fetch/<t>")
def fetch(t):
    n = 500
    bin = 1
    try:
        t = time.time() - float(t)

        water   = database.get_water(t)
        water   = sorted(water, key=lambda x: x['time'])
        # water   = moving_average(water, key='value', window_size=bin)
        water   = [{'time': sum([k['time'] for k in x]) / len(x), 'value': sum([k['value'] for k in x]) / len(x)} for x in split_list(water, n)]

        air   = database.get_air(t)
        air   = sorted(air, key=lambda x: x['time'])
        # air   = moving_average(air, key='value', window_size=bin)
        air   = [{'time': sum([k['time'] for k in x]) / len(x), 'value': sum([k['value'] for k in x]) / len(x)} for x in split_list(air, n)]

        humid   = database.get_humid(t)
        humid   = sorted(humid, key=lambda x: x['time'])
        humid   = moving_average(humid, key='value', window_size=bin)
        humid   = [{'time': sum([k['time'] for k in x]) / len(x), 'value': sum([k['value'] for k in x]) / len(x)} for x in split_list(humid, n)]

        voltage   = database.get_voltage(t)
        voltage   = sorted(voltage, key=lambda x: x['time'])
        # voltage   = moving_average(voltage, key='value', window_size=bin)
        voltage   = [{'time': sum([k['time'] for k in x]) / len(x), 'value': sum([k['value'] for k in x]) / len(x)} for x in split_list(voltage, n)]

        soc   = database.get_soc(t)
        soc   = sorted(soc, key=lambda x: x['time'])
        # soc   = moving_average(soc, key='value', window_size=bin)
        soc   = [{'time': sum([k['time'] for k in x]) / len(x), 'value': sum([k['value'] for k in x]) / len(x)} for x in split_list(soc, n)]

        return {'water': water, 'air': air, 'humid': humid, 'voltage': voltage, 'soc': soc}
    except Exception as e:
        return str(e)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)