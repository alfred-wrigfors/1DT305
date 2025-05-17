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
        

POWER_DRAW              = 1.5
POWER_DRAW_DURATION     = 2.0
POWER_DRAW_PERIOD       = 30.0

SOLAR_POWER             = 0.5
SOLAR_EFFICIENCY_FACTOR = 0.5

sun = Sun(10.0, 17.0, 1/2)
bat = Battery(2.5*3600, 3.7, 1.0)

soc = []
time = []
for i in range(60*60*24*31):
    solar   = sun.update(i / (60 * 60)) * SOLAR_POWER * SOLAR_EFFICIENCY_FACTOR
    device  = POWER_DRAW * (i % int(POWER_DRAW_PERIOD) in range(int(POWER_DRAW_DURATION)))
    soc.append(bat.update(device - solar, 1))
    # soc.append(device)
    time.append(i / (60.0*60.0*24))

plt.plot(time, soc)
plt.ylim(-0.1, 1.1)
plt.show()