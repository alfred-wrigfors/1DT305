from datetime import datetime
import pickle 


class Database:
    def __init__(self, location: str = "../.data/database.pkl"):
        self.location = location

        self.water  = []
        self.air    = []
        self.humid  = []

        self.__load__()

    def __load__(self) -> None:
        try:
            with open(self.location, "rb") as file:
                data = pickle.load(file)
                self.water  = data['water']
                self.air    = data['air']
                self.humid  = data['humid']
        except Exception:
            pass


    def __store__(self) -> None:
        try:
            with open(self.location, "wb") as file:
                pickle.dump({'water': self.water, 'air': self.air, 'humid': self.humid}, file)
        except Exception as e:
            print(e)
            pass

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
            self.__store__()
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
            self.__store__()
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
            self.__store__()
            return True
        except Exception:
            return False
