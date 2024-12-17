from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QDialog, QCheckBox, QGridLayout
from PyQt5.uic import loadUi
import sys
import json
import client_socketTCP
import time
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("//server/ivan.dimit22/Downloads/ETI 13.1/Smart_Home_Control/Smart_Home_Control_GUI_MainWindow.ui", self)
    
        self.__client_socket = None
        self.__pins = [11,13,15,16,18]
        self.__current_row = 1
        self.__current_devices = []
        self.__detect_button = None
        for i in range(1,6):
            edit_btns = getattr(self, f"btn_edit_{i}")
            edit_btns.setEnabled(False)
            edit_btns_clicked = getattr(self, f"btn_edit_{i}_clicked")
            edit_btns.clicked.connect(edit_btns_clicked)
            name_btns = getattr(self, f"btn_name_{i}")
            name_btns.setEnabled(False)
            name_btns_clicked = getattr(self, f"btn_name_{i}_clicked")
            name_btns.clicked.connect(name_btns_clicked)
        self.btn_add_device.clicked.connect(self.btn_add_device_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_import.clicked.connect(self.btn_import_clicked)
        self.btn_server_exit.clicked.connect(self.btn_server_exit_clicked)
        self.btn_server_connect.clicked.connect(self.btn_server_connect_clicked)
        self.btn_server_disconnect.clicked.connect(self.btn_sever_disconnect_clicked)

        self.btn_add_device.setEnabled(False)
        self.btn_export.setEnabled(False)
        self.btn_server_disconnect.setEnabled(False)

    def btn_name_1_clicked(self):
        dlg_control_device = ControlWindow(self)
        dlg_control_device.lbl_control_device_name_current.setText(self.btn_name_1.text())
        dlg_control_device.lbl_control_device_state_current.setText(self.lbl_state_1.text())
        dlg_control_device_status = dlg_control_device.exec_()
        print(self.btn_name_1.text())
        if dlg_control_device_status == QDialog.Accepted:
            new_state = dlg_control_device.lbl_control_device_state_current.text()
            self.lbl_state_1.setText(new_state)
            self.__current_devices[0][3] = new_state
            client_socketTCP.set_pin_state(self.__client_socket, self.__pins[0], new_state)
            print("Accepted control 1")
        elif dlg_control_device_status == QDialog.Rejected:
            print("Rejected control 1")

    def btn_name_2_clicked(self):
        dlg_control_device = ControlWindow(self)
        dlg_control_device.lbl_control_device_name_current.setText(self.btn_name_2.text())
        dlg_control_device.lbl_control_device_state_current.setText(self.lbl_state_2.text())
        dlg_control_device_status = dlg_control_device.exec_()
        print(self.btn_name_2.text())
        if dlg_control_device_status == QDialog.Accepted:
            new_state = dlg_control_device.lbl_control_device_state_current.text()
            self.lbl_state_2.setText(new_state)
            self.__current_devices[1][3] = new_state
            client_socketTCP.set_pin_state(self.__client_socket, self.__pins[1], new_state)
            print("Accepted control 2") 
        elif dlg_control_device_status == QDialog.Rejected:
            print("Rejected control 2")

    def btn_name_3_clicked(self):
        dlg_control_device = ControlWindow(self)
        dlg_control_device.lbl_control_device_name_current.setText(self.btn_name_3.text())
        dlg_control_device.lbl_control_device_state_current.setText(self.lbl_state_3.text())
        dlg_control_device_status = dlg_control_device.exec_()
        print(self.btn_name_3.text())
        if dlg_control_device_status == QDialog.Accepted:
            new_state = dlg_control_device.lbl_control_device_state_current.text()
            self.lbl_state_3.setText(new_state)
            self.__current_devices[2][3] = new_state
            client_socketTCP.set_pin_state(self.__client_socket, self.__pins[2], new_state)
            print("Accepted control 3")
        elif dlg_control_device_status == QDialog.Rejected:
            print("Rejected control 3")

    def btn_name_4_clicked(self):
        dlg_control_device = ControlWindow(self)
        dlg_control_device.lbl_control_device_name_current.setText(self.btn_name_4.text())
        dlg_control_device.lbl_control_device_state_current.setText(self.lbl_state_4.text())
        dlg_control_device_status = dlg_control_device.exec_()
        print(self.btn_name_4.text())
        if dlg_control_device_status == QDialog.Accepted:
            new_state = dlg_control_device.lbl_control_device_state_current.text()
            self.lbl_state_4.setText(new_state)
            self.__current_devices[3][3] = new_state
            client_socketTCP.set_pin_state(self.__client_socket, self.__pins[3], new_state)
            print("Accepted control 4")
        elif dlg_control_device_status == QDialog.Rejected:
            print("Rejected control 4")

    def btn_name_5_clicked(self):
        dlg_control_device = ControlWindow(self)
        dlg_control_device.lbl_control_device_name_current.setText(self.btn_name_5.text())
        dlg_control_device.lbl_control_device_state_current.setText(self.lbl_state_5.text())
        dlg_control_device_status = dlg_control_device.exec_()
        print(self.btn_name_5.text())
        if dlg_control_device_status == QDialog.Accepted:
            new_state = dlg_control_device.lbl_control_device_state_current.text()
            self.lbl_state_5.setText(new_state)
            self.__current_devices[4][3] = new_state
            client_socketTCP.set_pin_state(self.__client_socket, self.__pins[4], new_state)
            print("Accepted control 5")
        elif dlg_control_device_status == QDialog.Rejected:
            print("Rejected control 5")
            
    def btn_edit_1_clicked(self):
        dlg_edit_device = EditWindow(self)
        dlg_edit_device.le_edit_device_name.setText(self.btn_name_1.text())
        dlg_edit_device.le_edit_device_type.setText(self.lbl_type_1.text())
        dlg_edit_device.le_edit_device_location.setText(self.lbl_location_1.text())
        dlg_edit_device_status = dlg_edit_device.exec_()
        if dlg_edit_device_status == QDialog.Accepted:
            print("Accepted edit 1")
            device_name = dlg_edit_device.le_edit_device_name.text()
            device_type = dlg_edit_device.le_edit_device_type.text()
            device_location = dlg_edit_device.le_edit_device_location.text()
            self.__current_devices[0][0] = device_name
            self.__current_devices[0][1] = device_type
            self.__current_devices[0][2] = device_location
            self.btn_name_1.setText(device_name)
            self.lbl_type_1.setText(device_type)
            self.lbl_location_1.setText(device_location)
        elif dlg_edit_device_status == QDialog.Rejected:
            print("Declined edit 1")

    def btn_edit_2_clicked(self):
        dlg_edit_device = EditWindow(self)
        dlg_edit_device.le_edit_device_name.setText(self.btn_name_2.text())
        dlg_edit_device.le_edit_device_type.setText(self.lbl_type_2.text())
        dlg_edit_device.le_edit_device_location.setText(self.lbl_location_2.text())
        dlg_edit_device_status = dlg_edit_device.exec_()
        if dlg_edit_device_status == QDialog.Accepted:
            print("Accepted edit 2")
            device_name = dlg_edit_device.le_edit_device_name.text()
            device_type = dlg_edit_device.le_edit_device_type.text()
            device_location = dlg_edit_device.le_edit_device_location.text()
            self.__current_devices[1][0] = device_name
            self.__current_devices[1][1] = device_type
            self.__current_devices[1][2] = device_location
            self.btn_name_2.setText(device_name)
            self.lbl_type_2.setText(device_type)
            self.lbl_location_2.setText(device_location)
        elif dlg_edit_device_status == QDialog.Rejected:
            print("Declined edit 2")

    def btn_edit_3_clicked(self):
        dlg_edit_device = EditWindow(self)
        dlg_edit_device.le_edit_device_name.setText(self.btn_name_3.text())
        dlg_edit_device.le_edit_device_type.setText(self.lbl_type_3.text())
        dlg_edit_device.le_edit_device_location.setText(self.lbl_location_3.text())
        dlg_edit_device_status = dlg_edit_device.exec_()
        if dlg_edit_device_status == QDialog.Accepted:
            print("Accepted edit 3")
            device_name = dlg_edit_device.le_edit_device_name.text()
            device_type = dlg_edit_device.le_edit_device_type.text()
            device_location = dlg_edit_device.le_edit_device_location.text()
            self.__current_devices[2][0] = device_name
            self.__current_devices[2][1] = device_type
            self.__current_devices[2][2] = device_location
            self.btn_name_3.setText(device_name)
            self.lbl_type_3.setText(device_type)
            self.lbl_location_3.setText(device_location)
        elif dlg_edit_device_status == QDialog.Rejected:
            print("Declined edit 3")

    def btn_edit_4_clicked(self):
        dlg_edit_device = EditWindow(self)
        dlg_edit_device.le_edit_device_name.setText(self.btn_name_4.text())
        dlg_edit_device.le_edit_device_type.setText(self.lbl_type_4.text())
        dlg_edit_device.le_edit_device_location.setText(self.lbl_location_4.text())
        dlg_edit_device_status = dlg_edit_device.exec_()
        if dlg_edit_device_status == QDialog.Accepted:
            print("Accepted edit 4")
            device_name = dlg_edit_device.le_edit_device_name.text()
            device_type = dlg_edit_device.le_edit_device_type.text()
            device_location = dlg_edit_device.le_edit_device_location.text()
            self.__current_devices[3][0] = device_name
            self.__current_devices[3][1] = device_type
            self.__current_devices[3][2] = device_location
            self.btn_name_4.setText(device_name)
            self.lbl_type_4.setText(device_type)
            self.lbl_location_4.setText(device_location)
        elif dlg_edit_device_status == QDialog.Rejected:
            print("Declined edit 4")

    def btn_edit_5_clicked(self):
        dlg_edit_device = EditWindow(self)
        dlg_edit_device.le_edit_device_name.setText(self.btn_name_5.text())
        dlg_edit_device.le_edit_device_type.setText(self.lbl_type_5.text())
        dlg_edit_device.le_edit_device_location.setText(self.lbl_location_5.text())
        dlg_edit_device_status = dlg_edit_device.exec_()
        if dlg_edit_device_status == QDialog.Accepted:
            print("Accepted edit 5")
            device_name = dlg_edit_device.le_edit_device_name.text()
            device_type = dlg_edit_device.le_edit_device_type.text()
            device_location = dlg_edit_device.le_edit_device_location.text()
            self.__current_devices[4][0] = device_name
            self.__current_devices[4][1] = device_type
            self.__current_devices[4][2] = device_location
            self.btn_name_5.setText(device_name)
            self.lbl_type_5.setText(device_type)
            self.lbl_location_5.setText(device_location)
        elif dlg_edit_device_status == QDialog.Rejected:
            print("Declined edit 5")

    def btn_add_device_clicked(self):
        dlg_add_device = AddWindow(self)
        dlg_add_device_status = dlg_add_device.exec_()
        if dlg_add_device_status == QDialog.Accepted:
            if self.__current_row <= 5:
                print("Accepted add")
                device_name = dlg_add_device.le_add_device_name.text()
                device_type = dlg_add_device.le_add_device_type.text()
                device_location = dlg_add_device.le_add_device_location.text()
                self.grid_devices.itemAtPosition(self.__current_row, 0).widget().setText(device_name)
                self.grid_devices.itemAtPosition(self.__current_row, 1).widget().setText(device_type)
                self.grid_devices.itemAtPosition(self.__current_row, 2).widget().setText(device_location)
                self.grid_devices.itemAtPosition(self.__current_row, 2).widget().setText("False")
                self.__current_devices.insert(self.__current_row, [device_name, device_type, device_location, None])
                state_lbl = getattr(self, f"lbl_state_{self.__current_row}")
                state_lbl.setText("None")
                name_btn = getattr(self, f"btn_name_{self.__current_row}")
                name_btn.setEnabled(True)
                edit_btn = getattr(self, f"btn_edit_{self.__current_row}")
                edit_btn.setEnabled(True)
                client_socketTCP.set_pin_state(self.__client_socket, self.__pins[self.__current_row - 1], False)
                self.__current_row = self.__current_row + 1
                print(self.__current_devices)
                self.btn_export.setEnabled(True)

            else:
                 print("Rows are filled")
        elif dlg_add_device_status == QDialog.Rejected:        
            print("Rejected add")

    def btn_export_clicked(self):                            
        with open ("Smart_Home_Control/Smart_Home_Control_Data.json", "w") as file:
            json.dump(self.__current_devices, file)

    def btn_import_clicked(self):
        self.btn_export.setEnabled(True)
        try:
            with open ("Smart_Home_Control/Smart_Home_Control_Data.json", "r") as file:
                self.__current_devices = json.load(file)
                row_count = 0
                for nested_lists in self.__current_devices:
                    if isinstance(nested_lists, list):
                        if self.__current_devices[row_count][3] == "":
                            client_socketTCP.set_pin_state(self.__client_socket, self.__pins[row_count], False)
                            time.sleep(0.01)
                        else:
                            client_socketTCP.set_pin_state(self.__client_socket, self.__pins[row_count], self.__current_devices[row_count][3])
                            time.sleep(0.01)
                        row_count = row_count + 1
                column_count = self.grid_devices.columnCount()
                self.__current_row = row_count
                for i in range(row_count):
                    for j in range(column_count-1):
                        current_widget = self.grid_devices.itemAtPosition(i+1,j).widget()
                        current_widget.setText(self.__current_devices[i][j])
                        if current_widget.text() == "":
                            current_widget.setText("None")
                        if not isinstance(current_widget, QLabel):
                            current_widget.setEnabled(True)
                            self.grid_devices.itemAtPosition(i+1,4).widget().setEnabled(True)
        except AttributeError:
            print("AttributeError")

    def btn_server_exit_clicked(self):
        try:
            self.close()
            self.__client_socket.close()
        except:
            pass
    
    def btn_server_connect_clicked(self):
        self.__client_socket = client_socketTCP.establish_connection(self.le_server_ip.text())
        self.lbl_connection_status.setText(f"Ip-Address: {self.le_server_ip.text()}")
        self.btn_add_device.setEnabled(True)
        self.btn_server_disconnect.setEnabled(True)
        self.btn_server_connect.setEnabled(False)
        self.__detect_button = threading.Thread(target=self.detect_button_press)
        self.__detect_button.start()


    def btn_sever_disconnect_clicked(self):
        self.__client_socket.close()
        self.lbl_connection_status.setText(f"Ip-Address: None")
        self.btn_add_device.setEnabled(False)
        self.btn_export.setEnabled(False)
        self.btn_server_disconnect.setEnabled(False)

    def detect_button_press(self):
        while True:
            server_response = self.__client_socket.recv(1024).decode("utf-8")
            if server_response == "button_clicked":
                if self.__current_devices[0][3] == "False":
                    print("False")
                    self.lbl_state_3.setText("True")
                    self.__current_devices[0][3] = "True"

                elif self.__current_devices[0][3] == "True":
                    print("True")
                    self.lbl_state_3.setText("False")
                    self.__current_devices[0][3] == "False"





class AddWindow(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi("//server/ivan.dimit22/Downloads/ETI 13.1/Smart_Home_Control/Smart_Home_Control_GUI_add.ui", self)
        self.dglBtn_add.accepted.connect(self.accept)
        self.dglBtn_add.rejected.connect(self.reject)   

class ControlWindow(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi("//server/ivan.dimit22/Downloads/ETI 13.1/Smart_Home_Control/Smart_Home_Control_GUI_Control.ui", self)
        self.dglBtn_control.accepted.connect(self.accept)
        self.dglBtn_control.rejected.connect(self.reject)
        self.btn_control_state_on.clicked.connect(self.btn_control_state_on_clicked)
        self.btn_control_state_off.clicked.connect(self.btn_control_state_off_clicked)

    def btn_control_state_on_clicked(self):
        self.lbl_control_device_state_current.setText("True")
    def btn_control_state_off_clicked(self):
        self.lbl_control_device_state_current.setText("False")

class EditWindow(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi("//server/ivan.dimit22/Downloads/ETI 13.1/Smart_Home_Control/Smart_Home_Control_GUI_edit.ui", self)
        self.dglBtn_edit.accepted.connect(self.accept)
        self.dglBtn_edit.rejected.connect(self.reject)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
