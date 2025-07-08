import time
import pickle 

import os


class Database:
    def __init__(self, location: str = "../data/database.pkl"):
        self.location = location

        self.water      = []
        self.air        = []
        self.humid      = []
        self.voltage    = []
        self.soc        = []

        self.__load__()

    def __load__(self) -> None:
        try:
            with open(self.location, "rb") as file:
                data = pickle.load(file)
                self.water      = data['water']
                self.air        = data['air']
                self.humid      = data['humid']
                self.voltage    = data['voltage']
                self.soc        = data['soc']
        except Exception:
            pass


    def __store__(self) -> None:
        try:
            with open(self.location, "wb") as file:
                pickle.dump({'water': self.water, 'air': self.air, 'humid': self.humid, 'voltage': self.voltage, 'soc': self.soc}, file)
        except Exception as e:
            print(e)
            pass

    def __get_seconds__() -> float:
        return time.time()
    
    def get_water(self, duration: float) -> None:
        if len(self.water) < 1:
            return []
        
        data = [pair for pair in self.water.copy() if pair['time'] >= duration]

        return data

    def put_water(self, value: float, t: float | None = None) -> None:
        if t is None:
            t = time.time()

        try:
            self.water.append({'time': t, 'value': value})
            self.__store__()
            return True
        except Exception:
            return False

    def get_air(self, duration: float) -> None:
        if len(self.air) < 1:
            return []
        
        data = [pair for pair in self.air.copy() if pair['time'] >= duration]

        return data

    def put_air(self, value: float, t: float | None = None) -> None:
        if t is None:
            t = time.time()

        try:
            self.air.append({'time': t, 'value': value})
            self.__store__()
            return True
        except Exception:
            return False

    def get_humid(self, duration: float) -> None:
        if len(self.humid) < 1:
            return []
        
        data = [pair for pair in self.humid.copy() if pair['time'] >= duration]

        return data

    def put_humid(self, value: float, t: float | None = None) -> None:
        if t is None:
            t = time.time()

        try:
            self.humid.append({'time': t, 'value': value})
            self.__store__()
            return True
        except Exception:
            return False

    def put_voltage(self, value: float, t: float | None = None) -> None:
        if t is None:
            t = time.time()

        try:
            self.voltage.append({'time': t, 'value': value})
            self.__store__()
            return True
        except Exception:
            return False

    def get_voltage(self, duration: float) -> None:
        if len(self.voltage) < 1:
            return []
        
        data = [pair for pair in self.voltage.copy() if pair['time'] >= duration]

        return data
    
    def put_soc(self, value: float, t: float | None = None) -> None:
        if t is None:
            t = time.time()

        try:
            self.soc.append({'time': t, 'value': value})
            self.__store__()
            return True
        except Exception:
            return False

    def get_soc(self, duration: float) -> None:
        if len(self.soc) < 1:
            return []
        
        data = [pair for pair in self.soc.copy() if pair['time'] >= duration]

        return data

