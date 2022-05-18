# Creates a virtual serial port 
# Prints out whatever is sent to it in the terminal
#
# By Joseph Telaak, 2022

import pty
import tty
import os

# Create the port and print
def run():
    # Open port
    master_fd, slave_fd = pty.openpty()

    # Setup
    tty.setraw(master_fd)
    os.set_blocking(master_fd, False)

    # Open port
    master_file = open(master_fd, 'r+b', buffering=0)

    # Print name of new port
    print("Virtual Serial Port: " + os.ttyname(slave_fd))

    # Read port and print
    while True:
        # Read file
        data = master_file.read()

        # Print data
        if data != None:
            print(data)

# Main
def main():
    try:
        run()

    # Keyboard interrupt to exit
    except KeyboardInterrupt:
        print("Exiting....")
        pass

if __name__ == '__main__':
    main()
