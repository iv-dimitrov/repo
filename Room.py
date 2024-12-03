class Room:
    def __init__(self, room_no, name, current_temp, current_rel_humidity, target_temp, target_rel_humidity, thermometer, hygrometer):
        self.__room_no = room_no
        self.__name = name
        self.__current_temp = current_temp
        self.__current_rel_humidity = current_rel_humidity
        self.__target_temp = target_temp
        self.__target_rel_humidity = target_rel_humidity
        self.__thermometer = thermometer
        self.__hygrometer = hygrometer
    def simulate_current_temp(self, temp_step):
        self.__current_temp = self.__current_temp + temp_step
    def get_room_no(self):
        return self.__room_no
    def get_name(self):
        return self.__name
    def get_target_temp(self):
        return self.__target_temp
    def get_target_rel_humidity(self):
        return self.__target_rel_humidity
    def get_thermometer(self):
        return self.__thermometer
    def get_hygrometer(self):
        return self.__hygrometer
    def set_thermometer(self, thermometer_new):
        self.__thermometer = thermometer_new
    def set_hygrometer(self, hygrometer_new):
        self.__hygrometer = hygrometer_new
    def set_current_temp(self, new_temp):
        self.__current_temp = new_temp
    def get_current_temp(self):
        return self.__current_temp
