import matplotlib.pyplot as plt

V_IN = 3.3
PT_RANGE = [t / 10 for t in range(-150, 1150)]
PT_K = 0.385
RESISTORS = [90, 120]

res = [100 + t*PT_K for t in PT_RANGE]

def v_div(r1: float, r2: float, voltage: float = 3.3) -> float:
    return voltage * r2 / (r1 + r2)

def amp(v_pos: float, v_neg: float, gain: float = 1.0) -> float:
    return max(0, gain * (v_pos - v_neg))

temp = []
voltage = []

for t in PT_RANGE:
    resistance = 100.0 + t * PT_K
    v1 = v_div(max(RESISTORS), resistance)
    v2 = v_div(max(RESISTORS), min(RESISTORS))
    v_out = amp(v1, v2, 7.5)
    print(f"{t}, {v_out}")

    voltage.append(v_out)
    temp.append(t)

plt.plot(temp, voltage)
plt.xlabel('Temperature (deg C)')
plt.ylabel('Output (V)')
plt.title('Voltage vs temperature for PT100')
plt.grid()
plt.show()