# Importing Libraries
import serial


class Nunchuck_receiver:
    def __init__(self):
        self.arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

    def retrieve_data(self):
        self.arduino.reset_input_buffer()
        data = str(self.arduino.readline())
        print("Data: " + str(data))
        return data

    def send_matrix(self):
        self.arduino.write()
