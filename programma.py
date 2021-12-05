# install on arduino firmata => StandardFirmata
from pyfirmata import Arduino
import time

board = Arduino("COM11")
pin13 = board.get_pin("d:13:o")# digital/analog: pin ; in/out
pin12 = board.get_pin("d:12:o")# digital/analog: pin ; in/out
pin11 = board.get_pin("d:11:o")# digital/analog: pin ; in/out
pin10 = board.get_pin("d:10:o")# digital/analog: pin ; in/out

for i in range(6):
    # deg zalsh
    pin12.write(1)
    time.sleep(3)
    # mirgo zalsh
    for i in range(3):
        pin12.write(1)
        time.sleep(1)
        pin12.write(0)
        time.sleep(1)
    # deg dzeltens

    pin11.write(1)
    time.sleep(1)
    pin11.write(0)

    # deg sarkans

    pin10.write(1)
    time.sleep(3)
    pin10.write(0)

  # deg dzeltens

    pin11.write(1)
    time.sleep(1)
    pin11.write(0)