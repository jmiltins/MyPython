import time
import serial # pip install pyserial
from datetime import datetime, timedelta
from meteostat import Point, Daily, Hourly

#start = datetime(2021, 9, 23, 12, 00)
start = datetime.now() - timedelta(hours = 1)
end = datetime.now()
riga = Point(56.5648, 24.0626, 20)
data_hourly = Hourly(riga, start, end)
data_hourly = data_hourly.fetch()
print(data_hourly.temp)

arduino = serial.Serial('COM11', baudrate = 9600) # same as arduino
print('Established serial connection to Arduino')


while True:
    arduino_data = arduino.readline()
    print(arduino_data)
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    print(decoded_values.rstrip('\n'))
    print(data_hourly.temp)
    with open("weather.html", mode = 'w') as f:
        f.write(str(data_hourly.temp) + "\n")
        f.write(str(decoded_values) + "\n")
        time.sleep(3)
        arduino.flushInput()
