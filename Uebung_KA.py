# Importing necessary PyQt5 and Python modules
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QDialog, QCheckBox
from PyQt5.uic import loadUi
import sys
import Room
import Sensors
import random
import time
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Loading the UI from a file
        loadUi("//server/ivan.dimit22/Downloads/ETI 13.1/03.12/Uebung_KA.ui", self)
        # Disabling simulation buttons initially
        self.btn_show_sim_data.setEnabled(False)
        self.btn_exec_sim.setEnabled(False)
        # Initializing instance variables
        self.__room = None
        self.__thermometer = None
        self.__hygrometer = None
        self.__current_temp = None
        self.__absolute_humidity = None
        self.__relative_humidity = 0.45
        self.__sim_data = []
        # Connecting button clicks to respective functions
        self.btn_create_room.clicked.connect(self.btn_create_room_clicked)
        self.btn_exec_sim.clicked.connect(self.btn_exec_sim_clicked)
        self.btn_show_sim_data.clicked.connect(self.btn_show_sim_data_clicked)

    # Function to display simulation data in the browser
    def btn_show_sim_data_clicked(self):
        for row in self.__sim_data:
            self.brw.append(row)

    # Executes the simulation and updates labels
    def btn_exec_sim_clicked(self):
        self.lbl_relative_humidity.setText(f"rel. Luftfeuchtigkeit (IST): {str(45)}%")
        self.calculate_abs_humidity()  # Starts humidity calculation
        self.btn_exec_sim.setEnabled(False)
        time.sleep(0.5)  # Simulating delay
        self.btn_exec_sim.setEnabled(True)

    # Sets main window labels based on room, thermometer, and hygrometer data
    def set_mainwindow_labels(self):
        self.lbl_room_no.setText(f"Raum Nr.: {str(self.__room.get_room_no())}")
        self.lbl_room_name.setText(f"Raumbezeichnung: {self.__room.get_name()}")
        self.lbl_target_temp.setText(f"Temperatur (SOLL): {str(self.__room.get_target_temp())}")
        self.lbl_target_humidity.setText(f"Luftfeuchtigkeit (SOLL): {str(self.__room.get_target_rel_humidity())}")
        self.lbl_thermometer_id.setText(f"Thermometer-ID: {str(self.__thermometer.get_id())}")
        self.lbl_hygrometer_id.setText(f"Hygrometer-ID: {str(self.__hygrometer.get_id())}")

    # Function to create room and associated devices
    def btn_create_room_clicked(self):
        dlg_room_data_input = DlgRoomDataInput(self)
        self.btn_show_sim_data.setEnabled(False)
        self.btn_create_room.setEnabled(True)
        self.btn_exec_sim.setEnabled(True)
        dlg_room_data_input_status = dlg_room_data_input.exec_()
        if dlg_room_data_input_status == QDialog.Accepted:
            # Creating thermometer, hygrometer, and room objects with data from dialog
            self.__thermometer = Sensors.Thermometer(random.randint(1000,9999), "Thermo", None)
            self.__hygrometer = Sensors.Hygrometer(random.randint(1000,9999), "Hygro", None)
            self.__room = Room.Room(random.randint(1000,9999), dlg_room_data_input.le_name.text(), None, None, dlg_room_data_input.le_target_temp.text(), dlg_room_data_input.le_target_humidity.text(), self.__thermometer, self.__hygrometer)
            self.set_mainwindow_labels()

    # Function to calculate absolute humidity and update simulation data
    def calculate_abs_humidity(self):
        self.brw.append("Simulation gestartet.")
        self.__room.set_current_temp(float(self.le_starting_temp.text()))
        self.lbl_time.setText("Uhrzeit: 24:00")
        for time in range(12,25):
            # Calculate absolute humidity using formula
            self.__absolute_humidity = (6.112 * math.exp((17.67*self.__room.get_current_temp())/(self.__room.get_current_temp()+243.5))*self.__relative_humidity*2.1674)/(273.15+self.__room.get_current_temp()) 
            self.__absolute_humidity = round(self.__absolute_humidity,2)
            self.__room.simulate_current_temp(1)  # Simulate temperature change
            self.__sim_data.append(f"Zeit: {time}   Temp:{self.__room.get_current_temp()}C  RH:{self.__relative_humidity}%   AH:{self.__absolute_humidity}g/m3")
        # Update UI labels with current values
        self.lbl_current_temp.setText(f"Temperatur (IST): {str(self.__room.get_current_temp())}")
        self.lbl_absolute_humidity.setText(f"abs. Luftfeuchtigkeit (IST): {str(self.__absolute_humidity)}g/m3")
        self.btn_show_sim_data.setEnabled(True)
        self.brw.append("Simulation beendet")

# Dialog class for room data input
class DlgRoomDataInput(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi("//server/ivan.dimit22/Downloads/ETI 13.1/03.12/DlgRoomDataInput.ui", self)
        self.dlgBtn_set_room_data.accepted.connect(self.accept)
        self.dlgBtn_set_room_data.rejected.connect(self.reject)

# Main application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
