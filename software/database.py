from datetime import datetime

[31, 28, 31, 30, 31]

class Database:
    def __init__(self, location: str = "../.data/database"):
        self.location = location

        self.water  = []
        self.air    = []
        self.humid  = []

    def __get_seconds__() -> float:
        now = datetime.now()
        return 0.0 # TODO
    
    def get_water(self, duration: float) -> None:
        if len(self.water) < 1:
            return []
        
        data = [pair for pair in self.water if pair['time'] >= duration]

        return data

    def put_water(self, time: float, value: float) -> None:
        try:
            self.water.append({'time': time, 'value': value})
            return True
        except Exception:
            return False

    def get_air(self, duration: float) -> None:
        if len(self.air) < 1:
            return []
        
        data = [pair for pair in self.air if pair['time'] >= duration]

        return data

    def put_air(self, time: float, value: float) -> None:
        try:
            self.water.append({'time': time, 'value': value})
            return True
        except Exception:
            return False

    def get_humid(self, duration: float) -> None:
        if len(self.humid) < 1:
            return []
        
        data = [pair for pair in self.humid if pair['time'] >= duration]

        return data

    def put_humid(self, time: float, value: float) -> None:
        try:
            self.humid.append({'time': time, 'value': value})
            return True
        except Exception:
            return False
