import matplotlib.pyplot as plt

data    = []
values  = range(0, 1000)
PT = [100, 120]

def v_div(voltage: float, R1: float, R2: float) -> float:
    """Calculate the voltage divider output."""
    return voltage * R2 / (R1 + R2)

for value in values:
    v1 = v_div(3.3, PT[0], value)
    v2 = v_div(3.3, PT[1], value)
    data.append(abs(v1 - v2))

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