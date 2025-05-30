import matplotlib.pyplot as plt

class Sun:
    def __init__(self, start: float = 8.0, stop: float = 18.0, slope: float = 1/3):
        self.start  = start - 1.0 / slope
        self.stop   = stop  + 1.0 / slope
        self.slope  = slope
        
    def update(self, time: float):
        time = time % 24.0
        if time <= self.start or time >= self.stop:
            return 0
        
        start = max(min((time - self.start) * self.slope, 1), 0)
        stop  = max(min((self.stop - time)  * self.slope, 1), 0)
        return min(start, stop)

class Battery:
    def __init__(self, capacity: float = 2.5, voltage: float = 3.7, soc: float = 1.0):
        self.max_energy = capacity * voltage
        self.energy     = soc * self.max_energy
    
    def update(self, power, delta: float):
        self.energy -= power * delta
        self.energy = min(max(self.energy, 0), self.max_energy)
        return self.energy / self.max_energy
        

POWER_DRAW              = {
    "ESP32":    3.3 * 0.140,
    "TARVOS":   3.3 * 0.023,
    "DIODE":    0.7 * 0.200,
    "DC-DC":    0.2,
    "CHARGER":  0.1
}

POWER_DRAW              = sum(POWER_DRAW.values())

POWER_DRAW_DURATION     = 0.5
POWER_DRAW_PERIOD       = 10.0

SOLAR_POWER             = 0.5
SOLAR_EFFICIENCY_FACTOR = 0.38

sun = Sun(9.0, 17.5, 1/2)
bat = Battery(3.0*3600, 3.7, 1.0)

soc = []
time = []
for i in range(60*60*24*31 + 1):
    solar   = sun.update(i / (60 * 60)) * SOLAR_POWER * SOLAR_EFFICIENCY_FACTOR
    device  = POWER_DRAW * (i % int(POWER_DRAW_PERIOD) in range(int(POWER_DRAW_DURATION)))
    soc.append(bat.update(device - solar, 1))
    time.append(i / (60.0*60.0*24))
    if soc[-1] <= 0:
        break

print(str(int(i / (60.0 * 60.0 * 24.0))) + " days and " + str(int((i / (60.0 * 60.0)) % 24)) + " hours")

plt.plot(time, soc)
plt.ylim(-0.1, 1.1)
plt.show()