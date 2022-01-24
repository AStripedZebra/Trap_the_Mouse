# Importing Libraries
import serial

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

while True:
    data = str(arduino.readline())

    if data[2] == '1':
            print("Joystick 1 input:" + data[3] + "," + data[4])
    if data[2] == '2':
            print("Joystick 2 input:" + data[3] + "," + data[4])
