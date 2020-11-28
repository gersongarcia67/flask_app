#!/usr/bin/env python

import serial

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
        ser = serial.Serial('/dev/serial0', 115200, timeout=1)
        ser.flush()

        ser.write(b"B")
        blueRead=ser.readline().decode('utf-8').rstrip()


        ser.write(b"R")
        redRead=ser.readline().decode('utf-8').rstrip()


        ser.write(b"Y")
        yellowRead=ser.readline().decode('utf-8').rstrip()


        return "%s,%s,%s\n" % (blueRead,redRead,yellowRead)

@app.route("/b")
def b():
	ser = serial.Serial('/dev/serial0', 115200, timeout=1)
	ser.flush()

	ser.write(b"B")
	blueRead=ser.readline().decode('utf-8').rstrip()

	return "<p>%s</p>" % blueRead

@app.route("/r")
def r():
        ser = serial.Serial('/dev/serial0', 115200, timeout=1)
        ser.flush()

        ser.write(b"R")
        redRead=ser.readline().decode('utf-8').rstrip()

        return "<p>%s</p>" % redRead

@app.route("/y")
def y():
        ser = serial.Serial('/dev/serial0', 115200, timeout=1)
        ser.flush()

        ser.write(b"Y")
        yellowRead=ser.readline().decode('utf-8').rstrip()

        return "<p>%s</p>" % yellowRead



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

