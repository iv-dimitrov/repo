import random

class Sensor:
    def __init__(self, id, name):
        self._id = id   #int
        self._name = name   #str
    def get_id(self):
        return self._id #int

class Thermometer(Sensor):
    def __init__(self, id, name, current_temp):
        super().__init__(id, name)
        self.__curent_temp = current_temp
    def measure_temp(self):
        return self.__curent_temp


class Hygrometer(Sensor):
    def __init__(self, id, name, current_rel_humidity):
        super().__init__(id, name)
        self.__current_rel_humidity = current_rel_humidity
    def measure_rel_humidity(self):
        return self.__current_rel_humidity

