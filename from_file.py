# install on arduino firmata => StandardFirmata
from pyfirmata import Arduino
import time
state13 = False
board = Arduino("COM11")
pin13 = board.get_pin("d:13:o")# digital/analog: pin ; in/out

with open ("C:/123.txt") as f:
    for line in f:
        line = line.strip("\n")
        print(line)
        if int(line) == 13:
            print("Youu")
            state13 = not state13
            pin13.write(state13)
        
        time.sleep(1)


f.close()
        
        #file_pin = f.read

def change_state(pin):
     if int(line) == pin:
            print("Youu")
            state13 = not state13
            pin13.write(state13)