
import serial

ser = serial.Serial('/dev/serial0', 115200, timeout=1)
ser.flush()

ser.write(b"B")
blueRead=ser.readline().decode('utf-8').rstrip()

print(blueRead)
