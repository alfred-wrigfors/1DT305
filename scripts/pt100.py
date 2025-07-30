import matplotlib.pyplot as plt

def v_div(voltage: float, R1: float, R2: float) -> float:
    """Calculate the voltage divider output."""
    return voltage * R2 / (R1 + R2)

def resistance(values: list[float], pt: list[float]) -> list[float]:
    data = []
    for value in values:
        v1 = v_div(3.3, max(pt), value)
        v2 = v_div(3.3, min(pt), value)
        data.append(abs(v1 - v2))
    return data

data    = resistance(range(0, 1000), range(90, 147))
values  = range(0, 1000)


plt.plot(values, data)
plt.xlabel('Resistance (Ohms)')
plt.ylabel('Voltage Difference (V)')
plt.title('Voltage Difference vs Resistance for PT100')
plt.grid()
plt.show()

max = 0
index = 0

for i in range(len(data)):
    if data[i] > max:
        max = data[i]
        index = i

print(f'Max voltage difference: {max} V at resistance {values[index]} Ohms')