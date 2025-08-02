import matplotlib.pyplot as plt

BATTERY_CAPACITY = 3450 #mAh

class Sun:
    def __init__(self, start: float = 8.0, stop: float = 18.0, slope: float = 1/3):
        self.start  = start - 1.0 / slope
        self.stop   = stop  + 1.0 / slope
        self.slope  = slope
        
    def update(self, time: float):
        time = (time / (60 * 60)) % 24.0
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

class Device:
    def __init__(self, draw: float, idle: float, time: float | int, duty: float | int):
        self.draw = draw
        self.idle = idle
        self.time = time
        self.duty = duty
    
    def update(self, time: float):
        return self.draw if time % self.duty <= self.time else self.idle


SOLAR_POWER             = 0.55
SOLAR_EFFICIENCY_FACTOR = 0.4

sun = Sun(11.0, 17.5, 1/2)
battery = Battery((BATTERY_CAPACITY) / 1000 * 3600)
device = Device(0.175*3.3, 0.01, 3.5, 30)

soc = []
time = []
for i in range((60*60*24*31 + 1) * 10):
    t = i / 10
    solar   = sun.update(t) * SOLAR_POWER * SOLAR_EFFICIENCY_FACTOR
    esp     = device.update(t)
    soc.append(battery.update(esp - solar, 0.1))
    time.append(i / (60*60))
    if soc[-1] <= 0:
        break

print(str(int(i / (60.0 * 60.0 * 24.0 * 10))) + " days and " + str(int((i / (60.0 * 60.0 * 10)) % 24)) + " hours")

plt.plot([ t / (10*24)for t in time], soc)
plt.ylim(-0.1, 1.1)
plt.show()