# Importing Libraries
import serial


class Nunchuck_receiver:
    def __init__(self):
<<<<<<< Updated upstream
        self.arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
        
=======
        self.arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
>>>>>>> Stashed changes

    def request_data(self):
        self.arduino.write(bytes('r', 'utf-8'))

    def retrieve_data(self):
        data = str(self.arduino.readline())
        print(data)
        return data

    def send_matrix(self):
        self.arduino.write()
