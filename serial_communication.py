# Importing Libraries
import serial


class Serial_communication:
    def __init__(self):
        # set arduino communication
        self.arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

    # read and return all incoming data to update the players (Nunchuck input)
    def receive_data(self):
        data = str(self.arduino.readline())
        print("Data: " + str(data))
        return data

    # send all led matrix data to the arduino
    def send_data(self, p1, p2, mouse):
        message = "A"
        message += str(p1.grid_number)
        message += "B"
        message += str(p2.grid_number)
        message += "M"
        message += str(mouse.grid_number)

        #send the led grid as bytes
        self.arduino.write(message.encode())
