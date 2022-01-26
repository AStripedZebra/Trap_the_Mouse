# Importing Libraries
import serial


class Nunchuck_receiver:
    def __init__(self):
        self.arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)

    def retrieve_data(self):
        #self.arduino.reset_input_buffer()
        data = str(self.arduino.readline())
        print("Data: " + str(data))
        return data

    def send_data(self, p1, p2, mouse):
        message = "A"
        message += str(p1.grid_number)
        message += "B"
        message += str(p2.grid_number)
        message += "M"
        message += str(mouse.grid_number)
        self.arduino.write(message.encode())
