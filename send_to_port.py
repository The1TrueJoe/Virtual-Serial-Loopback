# Sends a message to our virtual serial port
#
# By Joseph Telaak, 2022

import sys
import serial # Pyserial 3.3

# Get port
if len(sys.argv) == 1:
    port = "/dev/ttys001"
else:
    port = str(sys.argv[1])

# Connect to our virtual port
serial_terminal = serial.Serial(port, 115200, timeout=.1)

# Send messages to the port
try:
    while True:
        message = input(">")
        serial_terminal.write(message.encode())

except KeyboardInterrupt:
    print("Exiting....")